'''
# Python code to illustrate append() mode 
file = open('axiom.txt','a') 
file.write("\nThis will add this line") 
file.close() 

'''
file = open('axiom.txt', 'r') 
print(file.read())
