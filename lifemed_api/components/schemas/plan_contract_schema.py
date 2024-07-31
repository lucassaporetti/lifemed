from pydantic import BaseModel


class PlanContractResponse(BaseModel):
    uuid: str
    patient_id: str
    plan_contract: str
    plan_id: str

    class Config:
        orm_mode = True


class PlanContractRequest(BaseModel):
    patient_id: str
    plan_contract: str
    plan_id: str
