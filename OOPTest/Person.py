# OPP - Person Class
class Person:
    
    
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def check(self):
        if self.age>=18:
         return True
        else:
         return False
    def show(self):
        return self.name+ " "+str(self.age) 
    

def Main():
    P=Person("Abc",12)
    print("Person Details"+P.show())
    if P.check():
        print(P.name+" is eligible to vote")
    else:
        print(P.name+" is not eligible to vote")


if __name__=="__main__":
    Main()



