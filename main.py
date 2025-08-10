
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
app = FastAPI()



app.include_router(auth.router)
app.include_router(users.router)

origins = [
    "http://localhost:8081",
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



