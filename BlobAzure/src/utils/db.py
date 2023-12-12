from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from BlobAzure.src.Repository.sale_data.query import TransactionRepository 
from BlobAzure.src.Repository.sample_employee_data.query import  EmployeeRepository
from dotenv import load_dotenv
import os

load_dotenv()

def init_db():
    try:
        postgres_host = os.getenv('PGHOST')
        postgres_port = os.getenv('PGPORT')
        postgres_db = os.getenv('PGDATABASE')
        postgres_user = os.getenv('PGUSER')
        postgres_password = os.getenv('PGPASSWORD')

        db_url = f"postgresql://{postgres_user}:{postgres_password}@{postgres_host}:{postgres_port}/{postgres_db}"

        # engine = create_engine(db_url)

        # CustomerBase.metadata.create_all(bind=engine)
        # TransactionBase.metadata.create_all(bind=engine)

        # Session = sessionmaker(bind=engine)
        # session = Session()

        transaction_repository = TransactionRepository(db_url=db_url)
        employee_repository = EmployeeRepository(db_url=db_url)

        return  transaction_repository,employee_repository

    except Exception as e:
        print(f"Error connecting to the database: {str(e)}")
        raise