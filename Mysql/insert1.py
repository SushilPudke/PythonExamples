# Enter the server name in host 
# followed by your user and 
# password along with the database 
# name provided by you. 

import mysql.connector 


mydb = mysql.connector.connect( 
host = "localhost", 
user = "root", 
password = "sushil@axiom", 
database = "axiom"
) 

mycursor = mydb.cursor() 

sql = "INSERT INTO Student (Name, Roll_no) VALUES (%s, %s)"
val = ("Ram", "85") 

mycursor.execute(sql, val) 
mydb.commit() 

print(mycursor.rowcount, "details inserted") 

# disconnecting from server 
mydb.close() 
