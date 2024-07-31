from sqlalchemy import (Column,
                        String
                        )

from lifemed_api.components.utils.database.service import Base


class Plan(Base):
    __tablename__ = 'plan_tb'

    uuid = Column(String, primary_key=True, index=True)
    description = Column(String)
    phones = Column(String)
