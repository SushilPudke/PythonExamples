# importing rquired libraries 
import mysql.connector 

dataBase = mysql.connector.connect( 
host ="localhost", 
user ="root", 
passwd ="sushil@axiom"
) 

# preparing a cursor object 
cursorObject = dataBase.cursor() 

# creating database 
cursorObject.execute("CREATE DATABASE school") 
