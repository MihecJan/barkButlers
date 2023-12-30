import mysql.connector

db_user = open("db/db_user.txt").read()
db_pass = open("db/db_pass.txt").read()
db_name = open("db/db_name.txt").read()

db = mysql.connector.connect(
    host="localhost",
    port=3306,
    user=db_user,
    password=db_pass,
    database=db_name
)

cursor = db.cursor()

sql_file = "db/insert_persons.sql"
query = ""
with open(sql_file, "r") as file:
    for line in file:
        if line == "\n":
            cursor.execute(query)
            query = ""
            continue

        query += line

db.commit()