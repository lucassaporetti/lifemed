from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AppointmentData(BaseModel):
    uuid: str
    patient_id: Optional[str]
    doctor_id: Optional[str]
    datetime: Optional[datetime]
    private: bool
    procedure_id: Optional[str]
    plan_contract_id: Optional[str]
