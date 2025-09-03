from pydantic import BaseModel, Field

class SignupMessage(BaseModel):
    id: int = Field(...)
    username: str = Field(min_length=2 ,max_length=255)
    email: str = Field(min_length=2 ,max_length=255)