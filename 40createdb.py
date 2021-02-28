import mysql.connector as mysql
mydb= mysql.connect(
    host = "localhost",
    user = "root",
    passwd=""
)

mycursor = mydb.cursor()

mycursor.execute("create database python2")
if mycursor:
    print("DB created successfully")
