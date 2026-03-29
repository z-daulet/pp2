from config import create_table , read_phonebook
from connect import db_connect
import pandas as pd


def parse_phonebook(path:str):
    return pd.read_csv(path)
def insert(df, conn):
    with conn.cursor() as cur:
        try:
            data = list(df[["username", "first_name", "phone_number"]].itertuples(index=False, name=None))
            query = """
                INSERT INTO phonebook(username, first_name, phone_number)
                VALUES (%s, %s, %s)
                ON CONFLICT(username) DO NOTHING
            """
            cur.executemany(query, data)
            conn.commit()
            print(f"Inserted {cur.rowcount} rows")
        except Exception as e:
            conn.rollback()
            print(f"Error occurred at insertion: {e}")

def delete(conn,credentials):
    with conn.cursor() as cur:
        try:
            query = """
                DELETE FROM phonebook WHERE username = %s 
            """
            cur.execute(query,credentials)
            conn.commit()
            print("Contact deleted")
        except Exception as e:
            conn.rollback()
            print(f"Error on delete: {e}")

def update(conn,credentials):
    with conn.cursor() as cur:
        try:
            query = """
                UPDATE phonebook SET first_name = %s, phone_number = %s WHERE username = %s 
            """
            cur.execute(query,("user1"))
            conn.commit()
            print("Contact updated")
        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")

def insert_terminal(conn, credentials):
    with conn.cursor() as cur:
        try:
            query = """
                INSERT INTO phonebook(username, first_name, phone_number) VALUES(%s,%s,%s)  
            """
            cur.execute(query,credentials)
            conn.commit()
            print("Contact added")
        except Exception as e:
            conn.rollback()
            print(f"Error: {e}")    
def read_contacts(conn,credentials):
        with conn.cursor() as cur:
            try:
                query = """
                    SELECT * FROM phonebook WHERE id BETWEEN %s AND %s  
                """
                cur.execute(query,credentials)
                print(cur.fetchall())
            except Exception as e:
                conn.rollback()
                print(f"Error: {e}") 

path ="./phonebook.csv"
phonebook_frame = parse_phonebook(path)
conn  = db_connect()
create_table(conn)
# insert(phonebook_frame, conn)
contacts = read_phonebook(conn)
# print(contacts)
# delete(conn, ("user1"))
# update(conn,("Beka","+77011234567", "user1"))
# terminal  = tuple(input("username, first_name, phonenumber: ").split())
# insert_terminal(conn, terminal)
# """"""""""""""""""""""""""
read_contacts(conn,("5","10"))
conn.close()