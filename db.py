import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Nan26@12345",
    database="salesdb"
)

print("Database Connected Successfully")