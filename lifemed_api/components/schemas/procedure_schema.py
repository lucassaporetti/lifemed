from pydantic import BaseModel


class ProcedureResponse(BaseModel):
    uuid: str
    name: str
    value: float

    class Config:
        orm_mode = True


class ProcedureRequest(BaseModel):
    uuid: str
    name: str
    value: float
