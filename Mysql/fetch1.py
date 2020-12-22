# fetch top row 
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM student")

myresult = mycursor.fetchone()

print(myresult)
