from .connection import get_connection, close_connection
from mysql.connector import *

conn = get_connection()
cursor = conn.cursor()

def create_tables():
    try:
        cursor.execute("""
        create table if not exists devices(
        device_id int primary key auto_increment,
        name varchar(100) not null,
        category varchar(50),
        location varchar(100),
        power_rating float check(power_rating>=0),
        status enum('active', 'inactive') default 'active'         
        )
        """)

        cursor.execute("""
        create table if not exists logs(
            log_id int primary key auto_increment,
            device_id int,
            timestamp datetime default current_timestamp,
            power_used float check(power_used>=0),
            duration int check(duration>=0),
            foreign key(device_id) references devices(device_id)
            )

        """)
        conn.commit()
        cursor.close()
        close_connection(conn)
        print("Table devices created successfully")
    except Error as e:
        print(f"Error creating table devices : {e}")

if __name__ == "__main__":
    create_tables()
