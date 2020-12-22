# Python code for creating Table in the Database 
# Host: It is the server name. It will be "localhost" 
# if you are using localhost database 

# import mysql.connectors as SQLC 
import mysql.connector 
def CreateTable(): 
	
	# Connecting To the Database in Localhost 
	DataBase = mysql.connector.connect( 
    host ="localhost", 
    user ="root", 
    passwd ="sushil@axiom",
    database ="school"
    )    

	# Cursor to the database 
	Cursor = DataBase.cursor() 
    

	# Query for Creating the table 
	# The student table contains two columns Name and 
	# Roll number of data types varchar i.e to store string 
	# and Roll number of the integer data type. 
	#RollNo,First_Name,Last_Name,Phone_Number,City,State,Age
	TableName ="CREATE TABLE Student( RollNo VARCHAR(10),First_Name VARCHAR(255), Last_Name VARCHAR(255),Phone_Number VARCHAR(255),City VARCHAR(255),State VARCHAR(255), Age VARCHAR(10));" 
					

	Cursor.execute(TableName) 
	print("Student Table is Created in the Database") 
	return

 # Calling CreateTable function 
CreateTable()