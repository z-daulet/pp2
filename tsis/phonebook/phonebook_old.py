# from connect import db_connect


# import csv
# import json
# import os
# from connect import db_connect

# def insert_from_csv(path="./contacts.csv", conn, cur):
#     with open(path, newline="", encoding="utf-8") as f:
#         reader = csv.DictReader(f)
#         for row in reader:
#             # Insert contact
#             cur.execute("""
#                 INSERT INTO contacts (first_name, last_name, email, birthday, group_id)
#                 VALUES (%s, %s, %s, %s, %s)
#                 RETURNING id
#             """, (
#                 row.get("first_name"),
#                 row.get("last_name"),
#                 row.get("email"),
#                 row.get("birthday") or None,
#                 row.get("group_id") or None,
#             ))
#             contact_id = cur.fetchone()[0]

#             # Insert phones if phones.csv exists
#             phones_path = "./phones.csv"
#             if os.path.exists(phones_path):
#                 with open(phones_path, newline="", encoding="utf-8") as pf:
#                     phones_reader = csv.DictReader(pf)
#                     for phone_row in phones_reader:
#                         if int(phone_row.get("contact_id", 0)) == contact_id:
#                             cur.execute("""
#                                 INSERT INTO phones (contact_id, phone, type)
#                                 VALUES (%s, %s, %s)
#                             """, (
#                                 contact_id,
#                                 phone_row.get("phone"),
#                                 phone_row.get("type"),
#                             ))

#     conn.commit()























# MENU = """
# ╔══════════════════════════════════════════════════╗
# ║         PhoneBook  –  TSIS 1 Extended Menu       ║
# ╠══════════════════════════════════════════════════╣
# ║  SCHEMA                                          ║
# ║  0.  Apply schema & procedures                   ║
# ╠══════════════════════════════════════════════════╣
# ║  SEARCH & FILTER                                 ║
# ║  1.  Filter contacts by group                    ║
# ║  2.  Search by email                             ║
# ║  3.  List all contacts (sorted)                  ║
# ║  4.  Browse contacts (paginated)                 ║
# ╠══════════════════════════════════════════════════╣
# ║  IMPORT / EXPORT                                 ║
# ║  5.  Export to JSON                              ║
# ║  6.  Import from JSON                            ║
# ║  7.  Import from CSV (extended)                  ║
# ╠══════════════════════════════════════════════════╣
# ║  STORED PROCEDURES                               ║
# ║  8.  Add phone number to contact                 ║
# ║  9.  Move contact to group                       ║
# ║  10. Search contacts (all fields + phones)       ║
# ╠══════════════════════════════════════════════════╣
# ║  Q.  Quit                                        ║
# ╚══════════════════════════════════════════════════╝
# """


# # HANDLERS = {
# #     "0":  init_schema,
# #     "1":  filter_by_group,
# #     "2":  search_by_email,
# #     "3":  sort_and_list,
# #     "4":  paginated_browse,
# #     "5":  export_to_json,
# #     "6":  import_from_json,
# #     "7":  insert_from_csv,
# #     "8":  call_add_phone,
# #     "9":  call_move_to_group,
# #     "10": call_search_contacts,
# # }

# HANDLERS = {
#     "0":  init_schema,
#     "1":  filter_by_group,
#     "2":  search_by_email,
#     "3":  sort_and_list,
#     "4":  paginated_browse,
#     "5":  export_to_json,
#     "6":  import_from_json,
#     "7":  insert_from_csv,
#     "8":  call_add_phone,
#     "9":  call_move_to_group,
#     "10": call_search_contacts,
# }

# def main():
#     while True:
#         print(MENU)
#         choice = input("Select option: ").strip().lower()
#         if choice == "q":
#             print("Goodbye!")
#             break
#         handler = HANDLERS.get(choice)
#         if handler:
#             try:
#                 handler()
#             except Exception as e:
#                 print(f"  ✗  Database error: {e}")
#         else:
#             print("  Invalid choice, please try again.")


# if __name__ == "__main__":
#     main()



# conn.close()