from kafka import KafkaProducer
from fastapi import HTTPException
import json
from producers.produce_schema import SignupMessage

# constants
KAFKA_BROKER = 'kafka1:9092'
KAFKA_TOPIC = 'user-events'
PRODUCER_CLIENT_ID = 'client-1'

def serializer(message: SignupMessage):
    return json.dumps(message.model_dump()).encode()

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=serializer,
    key_serializer=lambda k: k.encode('utf-8') if k else None,
    client_id=PRODUCER_CLIENT_ID,
)

def produce_kafka_signup_message(message: SignupMessage):
    try:
        producer.send(
            KAFKA_TOPIC,
            value=message,  # pass the Pydantic model directly
            key=str(message.id)
        )
        producer.flush()
        print("Message sent-----")
    except Exception as error:
        print(error)
        raise HTTPException(status_code=500, detail=f'Kafka Error: {error}')
