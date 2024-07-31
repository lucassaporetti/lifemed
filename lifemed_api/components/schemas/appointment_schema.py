from pydantic import BaseModel
from datetime import datetime


class AppointmentResponse(BaseModel):
    uuid: str
    patient_id: str
    doctor_id: str
    datetime: datetime
    private: bool
    procedure_id: str
    plan_contract_id: str

    class Config:
        orm_mode = True


class AppointmentRequest(BaseModel):
    patient_id: str
    doctor_id: str
    datetime: datetime
    private: bool
    procedure_id: str
    plan_contract_id: str
