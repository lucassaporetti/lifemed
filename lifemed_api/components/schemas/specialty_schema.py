from pydantic import BaseModel
from typing import Optional


class SpecialtyData(BaseModel):
    uuid: str
    name: Optional[str]
