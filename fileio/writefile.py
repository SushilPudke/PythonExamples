'''
# Python code to create a file 
file = open('newaxiom.txt','w') 
file.write("This is the write command \n ") 
file.write("It allows us to write in a particular file") 
file.close() 

'''
file = open('newaxiom.txt', 'r') 
print(file.read())
