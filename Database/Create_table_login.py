import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "0946192332",
    database="coffee"
)

mycursor = conn.cursor()

mycursor.execute("CREATE TABLE Register (\
    username VARCHAR(20) PRIMARY KEY UNIQUE KEY,\
    password CHAR(20) NOT NULL,\
    email VARCHAR(80) NOT NULL,\
    ")