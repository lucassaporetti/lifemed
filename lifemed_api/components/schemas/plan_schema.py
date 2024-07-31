from pydantic import BaseModel


class PlanResponse(BaseModel):
    uuid: str
    description: str
    phones: str

    class Config:
        orm_mode = True


class PlanRequest(BaseModel):
    description: str
    phones: str
