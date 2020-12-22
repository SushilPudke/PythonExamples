# Conditional Listing
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

# sql = "SELECT * FROM student WHERE name ='Amit' "
sql = "SELECT * FROM student WHERE roll_no<=50 "

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)