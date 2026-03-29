def create_table(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS phonebook(
                    id SERIAL PRIMARY KEY,
                    username VARCHAR(50) UNIQUE,
                    first_name VARCHAR(100) NOT NULL,
                    phone_number VARCHAR(20) NOT NULL UNIQUE
                )
            """)
            conn.commit()
            print("Table created")
    except Exception as e:
        conn.rollback()
        print(f"Error occured: {e}")
def read_phonebook(conn):
    try:
        with conn.cursor() as cur:
            cur.execute("""
                SELECT * from phonebook
            """)
            return cur.fetchall()
    except Exception as e:
        conn.rollback()
        print(f"Error occured: {e}")
