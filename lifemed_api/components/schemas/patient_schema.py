from pydantic import BaseModel
from datetime import date
from typing import Optional


class PatientData(BaseModel):
    uuid: str
    name: Optional[str]
    birth_date: Optional[date]
    phones: Optional[str]
    plan_linked: bool
