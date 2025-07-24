from typing import Annotated

from fastapi.params import Header


async def get_bearer_token(bearer_token : Annotated[str, Header]):
    print(bearer_token)