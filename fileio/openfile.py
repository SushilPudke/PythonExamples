# a file named "axiom", will be opened with the reading mode. 
#Demo -1 
'''
file = open('axiom.txt', 'r') 
# This will print every line one by one in the file 
for each in file: 
	print (each) 
'''
#Demo -2
# Python code to illustrate read() mode 
'''
file = open('axiom.txt', 'r') 
print(file.read())
'''
'''
# Python code to illustrate read() mode character wise 
file = open("axiom.txt", "r") 
print(file.read(5)) 
'''
