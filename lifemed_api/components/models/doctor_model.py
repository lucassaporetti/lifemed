from sqlalchemy import (Column,
                        String,
                        ForeignKey
                        )

from lifemed_api.components.utils.database.service import Base
from lifemed_api.components.models.specialty_model import Specialty


class Doctor(Base):
    __tablename__ = 'doctor_tb'

    uuid = Column(String, primary_key=True, index=True)
    name = Column(String)
    crm = Column(String)
    specialty_id = Column(String, ForeignKey(Specialty.uuid))
