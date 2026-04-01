from connect import db_connect

conn = db_connect()
def delete_query(filepath:str, conn):
    with open(filepath,"r") as file:
        sql_script = file.read()
    try:
        cursor = conn.cursor()
        cursor.execute(sql_script)

        print("Delete by:")
        print("1. Username")
        print("2. Phone number")
        print("3. Both username and phone number")
        choice = input("Choose option (1/2/3): ").strip()

        if choice == "1":
            username = input("Enter username: ").strip()
            cursor.execute("CALL delete_contact(%s, %s)", (username, None))
        elif choice == "2":
            phone = input("Enter phone number: ").strip()
            cursor.execute("CALL delete_contact(%s, %s)", (None, phone))
        elif choice == "3":
            username = input("Enter username: ").strip()
            phone = input("Enter phone number: ").strip()
            cursor.execute("CALL delete_contact(%s, %s)", (username, phone))
        else:
            print("Invalid option.")
            return

        conn.commit()
        print("Script executed")
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")

def upsert_query(filepath:str, conn):
    with open(filepath,"r") as file:
        sql_script = file.read()
    try:
        cursor = conn.cursor()
        cursor.execute(sql_script)

        print("Enter contact details to update:")
        username = input("Username to find: ").strip()
        new_name = input("New name: ").strip()
        new_phone = input("New phone number: ").strip()

        cursor.execute("CALL update_contact(%s,%s,%s)", (username, new_name, new_phone))
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

        print("Pagination options:")
        limit = int(input("How many rows per page (limit): ").strip())
        offset = int(input("Starting from row (offset): ").strip())

        cursor.execute("SELECT * FROM get_contacts_paginated(%s, %s);", (limit, offset))
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                print(row)
        else:
            print("No records found.")

        print("Script executed")
    except ValueError:
        print("Error: limit and offset must be integers.")
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
delete_query(filepath,conn)
# select_query(filepath_f,conn)
# insert_many(filepath, conn, contacts)
conn.close()