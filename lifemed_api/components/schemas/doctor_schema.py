from pydantic import BaseModel
from typing import Optional


class DoctorData(BaseModel):
    uuid: str
    name: Optional[str]
    crm: Optional[str]
    specialty_id: Optional[str]
