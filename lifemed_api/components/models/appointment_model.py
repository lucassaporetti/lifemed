from sqlalchemy import (String,
                        Column,
                        DateTime,
                        Boolean,
                        ForeignKey
                        )

from lifemed_api.components.utils.database.service import Base
from lifemed_api.components.models.procedure_model import Procedure
from lifemed_api.components.models.plan_contract_model import PlanContract
from lifemed_api.components.models.patient_model import Patient
from lifemed_api.components.models.doctor_model import Doctor


class Appointment(Base):
    __tablename__ = 'appointment_tb'

    uuid = Column(String, primary_key=True, index=True)
    patient_id = Column(String, ForeignKey(Patient.uuid))
    doctor_id = Column(String, ForeignKey(Doctor.uuid))
    datetime = Column(DateTime)
    private = Column(Boolean, nullable=False, default=True)
    procedure_id = Column(String, ForeignKey(Procedure.uuid))
    plan_contract_id = Column(String, ForeignKey(PlanContract.uuid))
