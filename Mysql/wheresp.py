# fetch having sp character
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="sushil@axiom",
  database="axiom"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM student WHERE name LIKE 'A%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)