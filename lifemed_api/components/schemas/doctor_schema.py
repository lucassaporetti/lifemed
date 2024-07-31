from pydantic import BaseModel


class DoctorResponse(BaseModel):
    uuid: str
    name: str
    crm: str
    specialty_id: str

    class Config:
        orm_mode = True


class DoctorRequest(BaseModel):
    name: str
    crm: str
    specialty_id: str
