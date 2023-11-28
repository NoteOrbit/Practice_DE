from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .model import *
import pandas as pd
from BlobAzure.src.utils.common.etl_utils import show_dataframe


class EmployeeRepository:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def create_transaction(self, transaction_data):
        new_transaction = Employee(**transaction_data)
        with self.Session() as session:
            session.add(new_transaction)
            session.commit()

    def get_all_transactions(self):
        with self.Session() as session:
            transactions = session.query(Employee).all()

            
            df = pd.DataFrame([
                {key: value for key, value in transaction.__dict__.items() if key != '_sa_instance_state'}
                for transaction in transactions
            ])

            
            show_dataframe("Employee", "All Employee", df)

            return df