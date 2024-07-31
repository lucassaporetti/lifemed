from sqlalchemy import (Column,
                        String,
                        Float
                        )

from lifemed_api.components.utils.database.service import Base


class Procedure(Base):
    __tablename__ = 'procedure_tb'

    uuid = Column(String, primary_key=True, index=True)
    name = Column(String)
    value = Column(Float)
