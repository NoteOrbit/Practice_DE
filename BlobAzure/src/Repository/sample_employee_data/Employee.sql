CREATE TABLE transactions (
    Transaction_ID SERIAL PRIMARY KEY,
    Customer_ID INTEGER,
    Product_ID INTEGER,
    Product_Category VARCHAR(50) NOT NULL,
    Quantity INTEGER,
    Unit_Price INTEGER,
    Sales_Amount INTEGER,
    Transaction_Date DATE,
    Total_price INTEGER
);


