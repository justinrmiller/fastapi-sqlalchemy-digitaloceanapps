from pydantic import BaseModel


class Details(BaseModel):
    version: str
    env: str
