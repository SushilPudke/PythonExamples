# deleting Sp. record
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

# sql = "DELETE FROM student WHERE name = 'Amit'"
sql = "DELETE FROM student WHERE roll_no<=50 "
mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

# Code to Drop Table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

sql = "DROP TABLE student"

mycursor.execute(sql)
