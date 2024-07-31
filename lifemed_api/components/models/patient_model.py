from sqlalchemy import (Column,
                        String,
                        Date,
                        Boolean
                        )

from lifemed_api.components.utils.database.service import Base


class Patient(Base):
    __tablename__ = 'patient_tb'

    uuid = Column(String, primary_key=True, index=True)
    name = Column(String)
    birth_date = Column(Date)
    phones = Column(String)
    plan_linked = Column(Boolean, nullable=False)
