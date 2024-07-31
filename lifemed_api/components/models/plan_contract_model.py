from sqlalchemy import (Column,
                        String,
                        ForeignKey
                        )

from lifemed_api.components.utils.database.service import Base
from lifemed_api.components.models.patient_model import Patient
from lifemed_api.components.models.plan_model import Plan


class PlanContract(Base):

    __tablename__ = 'plan_contract_tb'
    uuid = Column(String, primary_key=True, index=True)
    patient_id = Column(String, ForeignKey(Patient.uuid))
    plan_contract = Column(String)
    plan_id = Column(String, ForeignKey(Plan.uuid))
