from sqlalchemy import Integer, String ,Date,Column,Sequence
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

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
    seq = Sequence('employees_id_seq',start=1)
    __tablename__ = "employees"
    employee_id = Column(Integer, seq, primary_key=True,server_default=seq.next_value(),autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    job_title = Column(String(50), nullable=False)
    hire_date = Column(Date)
    salary = Column(Integer)


    def __repr__(self):
        return (
            f"<Employee("
            f"employee_id={self.employee_id}, "
            f"first_name='{self.first_name}', "
            f"last_name='{self.last_name}', "
            f"job_title='{self.job_title}', "
            f"hire_date={self.hire_date}, "
            f"salary={self.salary})"
            f">"
        )