import mysql.connector


db = mysql.connector.connect(
    host="localhost",
    port=3307,
    user="root",
    password="",
    database="barkbutlers"
)

cursor = db.cursor()

sql_file = "db/insert_persons.sql"
query = ""
with open(sql_file, "r") as file:
    for line in file:
        if line == "\n":
            print(query)
            cursor.execute(query)
            query = ""
            continue

        query += line

db.commit()