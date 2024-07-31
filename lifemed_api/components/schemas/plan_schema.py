from pydantic import BaseModel
from typing import Optional


class PlanData(BaseModel):
    uuid: str
    description: Optional[str]
    phones: Optional[str]
