import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="python"
)

mycursor = mydb.cursor()

msql = "SELECT * FROM customers WHERE   address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(msql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
print(mycursor.rowcount)