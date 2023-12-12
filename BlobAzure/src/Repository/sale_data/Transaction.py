from sqlalchemy import Integer, String ,Date,Column,Sequence 
from sqlalchemy.ext.declarative import declarative_base



Base = declarative_base()

class Transaction(Base):


    """
    Represents the 'Transaction' table in the database.

    Attributes:
        Transaction_ID (int): Primary key for the transaction.
        Customer_ID (int): ID of the customer associated with the transaction.
        Product_ID (int): ID of the product associated with the transaction.
        Product_Category (str): Category of the product (maximum length 50 characters).
        Quantity (int): Quantity of the product in the transaction.
        Unit_Price (int): Unit price of the product.
        Sales_Amount (int): Total sales amount for the transaction.
        Transaction_Date (datetime.date): Date of the transaction.
        Total_price (int): Total price for the transaction.
    """
    seq = Sequence('transactions_id_seq',start=1)
    __tablename__ = "transactions"
    Transaction_ID = Column(Integer,seq, primary_key=True,server_default=seq.next_value(),autoincrement=True)
    Customer_ID = Column(Integer)
    Product_ID = Column(Integer)
    Product_Category = Column(String(50), nullable=False)
    Quantity = Column(Integer)
    Unit_Price =Column(Integer)
    Sales_Amount = Column(Integer)
    Transaction_Date = Column(Date)
    Total_price = Column(Integer)


    def __repr__(self):
        return (
            f"<Transaction("
            f"Transaction_ID={self.Transaction_ID}, "
            f"Customer_ID={self.Customer_ID}, "
            f"Product_ID={self.Product_ID}, "
            f"Product_Category='{self.Product_Category}', "
            f"Quantity={self.Quantity}, "
            f"Unit_Price={self.Unit_Price}, "
            f"Sales_Amount={self.Sales_Amount}, "
            f"Transaction_Date={self.Transaction_Date}, "
            f"Total_price={self.Total_price})"
            f">"
        )
        
