# Demo Array of objects
class Bank:
    def __init__(self, dname,acno,amtbal):
        self.dname=dname
        self.acno=acno 
        self.amtbal=amtbal
    
    def display(self):
        print(f'Depositor Name:{self.dname},Account no:{self.acno} Amount Balance:{self.amtbal}')

# creating list	 
list = [] 

# appending instances to list 
list.append( Bank('Amit',100,5000) ) 
list.append( Bank('Deependra',200,8000) ) 
list.append( Bank('Sangita', 300,10000) ) 

for obj in list: 
	obj.display()

# We can also access instances attributes 
# as list[0].name, list[0].roll and so on. 
