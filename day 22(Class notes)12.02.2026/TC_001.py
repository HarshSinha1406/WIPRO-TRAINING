import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root123",
    database="feb2026"
)

cursor = conn.cursor()
print("Connected successfully")

cursor.execute("SELECT * FROM employee")

for row in cursor.fetchall():
    print(row)

conn.close()
