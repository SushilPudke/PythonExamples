# importing rquired libraries 
import mysql.connector 

dataBase = mysql.connector.connect( 
host ="localhost", 
user ="root", 
passwd ="sushil@axiom",
database="axiom"
) 

# preparing a cursor object 
cursorObject = dataBase.cursor() 

# creating database 
# cursorObject.execute("CREATE TABLE Student( Name VARCHAR(255), Name Roll_no  int);")
#print("DataBase Axiom Created") 

sql = "INSERT INTO Student (Name, Roll_no) VALUES (%s, %s)"
val = [("Akash", "98"), 
       ("Neel", "23"), 
       ("Rohan", "43"), 
       ("Amit", "87"), 
       ("Anil", "45"),  
       ("Megha", "55"),  
       ("Sita", "95")] 
  
cursorObject.executemany(sql, val) 
dataBase.commit() 
  
print(cursorObject.rowcount, "details inserted") 
  
# disconnecting from server 
dataBase.close() 