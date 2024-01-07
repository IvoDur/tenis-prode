from pydantic import BaseModel
from typing import Optional


class Match(BaseModel):
    Tr1: int
    Tr2: int
    Tr1S1: Optional[int]
    Tr2S1: Optional[int]
    Tr1S2: Optional[int]
    Tr2S2: Optional[int]
    Tr1S3: Optional[int]
    Tr2S3: Optional[int]


class Official_Match(Match):
    Eid: str
    T1: dict
    T2: dict
    Eps: str
    Esid: int
    Epr: int
    Ewt: int
    Esd: str
    Edf: str


class Custom_Match(Match):
    _id: Optional[str]
    T1: str
    T2: str
    Finished: bool
    Who_won: int
