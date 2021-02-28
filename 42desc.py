import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="python"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM test1 LIMIT 0")
print (mycursor.description)