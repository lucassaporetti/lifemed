from pydantic import BaseModel
from datetime import date


class PatientResponse(BaseModel):
    uuid: str
    name: str
    birth_date: date
    phones: str
    plan_linked: bool

    class Config:
        orm_mode = True


class PatientRequest(BaseModel):
    name: str
    birth_date: date
    phones: str
    plan_linked: bool
