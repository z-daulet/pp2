from connect import db_connect

conn = db_connect()
def upsert_query(filepath:str, conn):
    with open(filepath,"r") as file:
        sql_script = file.read()
    try:
        cursor = conn.cursor()
        cursor.execute(sql_script)
        cursor.execute("CALL update_contact(%s,%s,%s)",("user1","Erzhan","+111111"))
        conn.commit()
        print("Script executed")
    except Exception as e:
        conn.rollback()   
        print(f"Error: {e}") 

def delete_query(filepath:str, conn):
    with open(filepath,"r") as file:
        sql_script = file.read()
    try:
        cursor = conn.cursor()
        cursor.execute(sql_script)
        cursor.execute("CALL delete_contact(%s)",("user1",))
        conn.commit()
        print("Script executed")
    except Exception as e:
        conn.rollback()   
        print(f"Error: {e}")
def select_query(filepath:str, conn):
    with open(filepath,"r") as file:
        sql_script = file.read()
    try:
        cursor = conn.cursor()
        cursor.execute(sql_script)
        cursor.execute("SELECT * FROM get_contacts_paginated(%s, %s);",(5,0))
        print(cursor.fetchall())
        # conn.commit()
        print("Script executed")
    except Exception as e:
        conn.rollback()   
        print(f"Error: {e}")    

def insert_many(filepath:str, conn, data:list[dict]):
    with open(filepath,"r") as file:
        sql_script = file.read()
    try:
        cursor = conn.cursor()
        cursor.execute(sql_script)
        contact_rows = []
        for d in data:
            contact_rows.append(
                f"ROW('{d['username']}','{d['first_name']}','{d['phone_number']}')::user_input"
            )
        user_array_sql = "ARRAY[" + ",".join(contact_rows) + "]"
        
        cursor.execute(f"CALL insert_many_contacts({user_array_sql});")

        conn.commit()
        print("Script executed")
    except Exception as e:
        conn.rollback()   
        print(f"Error: {e}")    



# правильный формат
contacts = [
    {"username": "user50", "first_name": "Alice", "phone_number": "+77012345678"},
    {"username": "user51", "first_name": "Karl", "phone_number": "+77098765432"},
    {"username": "user52", "first_name": "Bryan", "phone_number": "+77098765442"}
]
filepath = "./procedures.sql"
filepath_f = "./functions.sql"
# upsert_query(filepath, conn)
# delete_query(filepath,conn)
# select_query(filepath_f,conn)
insert_many(filepath, conn, contacts)
conn.close()