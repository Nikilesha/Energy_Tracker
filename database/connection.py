import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv("HOST"),
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            database=os.getenv("DATABASE")
        )
        print("✅ Connection successful")
        return conn
    except Error as e:
        print(f"Error: {e}")
        return None

def close_connection(conn):
    if conn and conn.is_connected():
        conn.close()
        print("✅ Connection closed")
