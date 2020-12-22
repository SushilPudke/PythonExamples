import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

sql = "UPDATE Student SET rollno = 102 WHERE name = 'Amit'"

mycursor.execute(sql)

mydb.commit()

print(mycursor.rowcount, "record(s) affected")

# Code for fetching Limit
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Student LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# fetch from from 3
  import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)