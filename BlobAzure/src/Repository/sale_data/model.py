from sqlalchemy import Integer, String ,Date
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column


class Base(DeclarativeBase):
    pass


class Transaction(Base):
    __tablename__ = "Transaction"
    Transaction_ID = mapped_column(Integer,primary_key=True)
    Customer_ID = mapped_column(Integer)
    Product_ID = mapped_column(Integer)
    Product_Category = mapped_column(String(50), nullable=False)
    Quantity = mapped_column(Integer)
    Unit_Price =mapped_column(Integer)
    Sales_Amount = mapped_column(Integer)
    Transaction_Date = mapped_column(Date)
    Total_price = mapped_column(Integer)


