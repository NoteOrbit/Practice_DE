from sqlalchemy import Integer, String ,Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


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
    __tablename__ = "transactions"
    Transaction_ID = mapped_column(Integer,primary_key=True)
    Customer_ID = mapped_column(Integer)
    Product_ID = mapped_column(Integer)
    Product_Category = mapped_column(String(50), nullable=False)
    Quantity = mapped_column(Integer)
    Unit_Price =mapped_column(Integer)
    Sales_Amount = mapped_column(Integer)
    Transaction_Date = mapped_column(Date)
    Total_price = mapped_column(Integer)


