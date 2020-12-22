'''
# Python code to illustrate with() 
with open("axiom.txt") as file:
    data = file.read()
    print(data) 
# do something with data 

'''
# Python code to illustrate with() alongwith write() 
with open("test.txt", "w") as f: 
	f.write("Hello World!!!") 