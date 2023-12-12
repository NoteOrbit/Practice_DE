from dotenv import load_dotenv
import os
import psycopg2
import logging

def create_db_connection():
    connection = None
    load_dotenv()
    try:
        connection = psycopg2.connect(
            database=os.getenv("DB_NAME"), 
            user=os.getenv("DB_USER"), 
            password=os.getenv("DB_PASSWORD"), 
            host=os.getenv("DB_HOST"), 
            port=os.getenv("DB_PORT")
        )
        print("Connection to PostgreSQL DB successful")
    except Exception as e:
        print(f"The error '{e}' occurred")

    return connection


def execute(table_name, column, start_timestamp, end_timestamp, conn):
    
    try:
        with conn.cursor() as cursor:
            query = f'SELECT DISTINCT "{column}" FROM "DBO"."{table_name}" WHERE "{column}" BETWEEN \'{start_timestamp}\' AND \'{end_timestamp}\''
            cursor.execute(query)
            rows = cursor.fetchall()

            logging.info(f"Executed query: {query}")
            logging.info(f"Rows returned: {len(rows)}")
        return [row for row in rows]
    except Exception as e:
        print(f"An error occurred: {e}")
