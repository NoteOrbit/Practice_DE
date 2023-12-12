from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .Transaction import *
import pandas as pd
from BlobAzure.src.utils.common.etl_utils import  show_dataframe


class TransactionRepository:
    def __init__(self, db_url):
        engine = create_engine(db_url)
        Base.metadata.create_all(engine)
        self.Session = sessionmaker(bind=engine)

    def create_transaction(self, args):
        new_transaction = Transaction(**args)
        print(new_transaction)
        with self.Session() as session:
            session.add(new_transaction)
            session.commit()
        
    def get_all_transactions(self):
        with self.Session() as session:
            transactions = session.query(Transaction).all()
 
            df = pd.DataFrame([
                {key: value for key, value in transaction.__dict__.items() if key != '_sa_instance_state'}
                for transaction in transactions
            ])

            show_dataframe("Transaction", "All Transactions", df)

            return df