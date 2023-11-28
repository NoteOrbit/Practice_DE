from sqlalchemy import Integer, String ,Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Employee(Base):


        """
    Represents the 'Employee' table in the database.

    Attributes:
        employee_id (int): Primary key for the employee.
        first_name (str): First name of the employee (maximum length 50 characters).
        last_name (str): Last name of the employee (maximum length 50 characters).
        job_title (str): Job title of the employee (maximum length 50 characters).
        hire_date (datetime.date): Date when the employee was hired.
        salary (int): Salary of the employee.


    """

    
    __tablename__ = "Employee"
    employee_id = mapped_column(Integer,primary_key=True)
    first_name = mapped_column(String(50), nullable=False)
    last_name = mapped_column(String(50), nullable=False)
    job_title = mapped_column(String(50), nullable=False)
    hire_date = mapped_column(Date)
    salary = mapped_column(Integer)


