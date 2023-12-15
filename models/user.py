from pydantic import BaseModel
from typing import Optional


class User(BaseModel):
    _id: Optional[str]
    mail: str
    username: str
    name: str
    last_name: str
    password: str
