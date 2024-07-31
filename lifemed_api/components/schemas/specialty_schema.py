from pydantic import BaseModel


class SpecialtyResponse(BaseModel):
    uuid: str
    name: str

    class Config:
        orm_mode = True


class SpecialtyRequest(BaseModel):
    name: str
