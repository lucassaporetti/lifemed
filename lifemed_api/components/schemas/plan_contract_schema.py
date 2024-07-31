from pydantic import BaseModel
from typing import Optional


class PlanContractData(BaseModel):
    uuid: str
    patient_id: Optional[str]
    plan_contract: Optional[str]
    plan_id: Optional[str]
