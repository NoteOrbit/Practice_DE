from sqlalchemy import Integer, String ,Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = "Employee"
    employee_id = mapped_column(Integer,primary_key=True)
    first_name = mapped_column(String(50), nullable=False)
    last_name = mapped_column(String(50), nullable=False)
    job_title = mapped_column(String(50), nullable=False)
    hire_date = mapped_column(Date)
    salary = mapped_column(Integer)


