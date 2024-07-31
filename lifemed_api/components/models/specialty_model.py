from sqlalchemy import (Column,
                        String
                        )

from lifemed_api.components.utils.database.service import Base


class Specialty(Base):
    __tablename__ = 'specialty_tb'

    uuid = Column(String, primary_key=True, index=True)
    name = Column(String)
