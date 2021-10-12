# from psycopg2 import DATETIME
from sqlalchemy import Column, VARCHAR, FLOAT, TEXT, DateTime
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class TestResultModel(Base):
    __tablename__ = "test_result"

    id = Column(VARCHAR(37), primary_key=True)
    name = Column(VARCHAR(100))
    result = Column(VARCHAR(10))
    date_created = Column(DateTime)
    type = Column(VARCHAR(10))
    duration = Column(FLOAT)
    log = Column(TEXT)
    std_error = Column(TEXT)
    std_out = Column(TEXT)
