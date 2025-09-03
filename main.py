
from functools import lru_cache

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError

from starlette.middleware.cors import CORSMiddleware
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

import config
from routes import auth , users
from time import  time

from kafka.admin import KafkaAdminClient, NewTopic
from contextlib import asynccontextmanager

# Constants
KAFKA_BROKER =  'kafka1:9092'
KAFKA_TOPIC = 'user-events'
KAFKA_ADMIN_CLIENT = 'auth_admin_client'


@asynccontextmanager
async def lifespan(app: FastAPI):
    admin_client = None
    try:
        for _ in range(5):
            try:
                admin_client = KafkaAdminClient(
                    bootstrap_servers=KAFKA_BROKER,
                    client_id=KAFKA_ADMIN_CLIENT,
                )
                break
            except Exception as e:
                print(f"Kafka not ready, retrying... {e}")
                time.sleep(2)

        if not admin_client:
            raise RuntimeError("Failed to connect to Kafka after retries")

        existing_topics = admin_client.list_topics()
        if KAFKA_TOPIC not in existing_topics:
            admin_client.create_topics([
                NewTopic(name=KAFKA_TOPIC, num_partitions=1, replication_factor=1)
            ])
            print(f"Topic '{KAFKA_TOPIC}' created.")
        else:
            print(f"Topic '{KAFKA_TOPIC}' already exists.")

        yield  # App runs here

    finally:
        if admin_client:
            admin_client.close()


app = FastAPI(lifespan=lifespan)



app.include_router(auth.router)
app.include_router(users.router)

origins = [
    "http://localhost:8085",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc) -> JSONResponse:
    print(f"PATH :{request.url.path}")
    print(f"Exception :{exc.detail}")
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.detail},
    )


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc) -> JSONResponse:
    return JSONResponse(
        status_code=400,
        content={"detail": jsonable_encoder(exc.errors())},
    )

@lru_cache
def get_settings():
    return config.Settings

@app.get("/")
async def root():
    return JSONResponse({"hello": "world"})



