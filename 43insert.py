import mysql.connector as mysql

mydb = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "python"
)

mycursor = mydb.cursor()
statement = "INSERT INTO test1(slno, name, class, marks) VALUES (%s,%s,%s,%s)"

val =(1,"lokesh","1 year",72)
mycursor.execute(statement, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")