# Display Columnwise data
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT roll_no FROM student")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)