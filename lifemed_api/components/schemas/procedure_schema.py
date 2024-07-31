from pydantic import BaseModel
from typing import Optional


class ProcedureData(BaseModel):
    uuid: str
    name: Optional[str]
    value: Optional[float]
