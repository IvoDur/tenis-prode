from pydantic import BaseModel
from typing import Optional


class Match(BaseModel):
    _id: Optional[str]
