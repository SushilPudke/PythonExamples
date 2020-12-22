# OOP- Arith Class 

class Arith:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def display(self):
        return f'a :{self.a} b :{self.b}'
    
    def add(self):
        return (self.a+self.b)

    def sub(self):
        return (self.a-self.b)

    def mul(self):
        return (self.a*self.b)
    def div(self):
        return (self.a/self.b)
    def mod(self):
        return (self.a % self.b)


def Main():
    at=Arith(5,7)
    print("Nos for Arithmetics "+at.display())
    print(f'Addition:{at.add()} ,Substraction:{at.sub()},Multilplication :{at.mul()},Divide:{at.div()},Modulus:{at.mod()}')


if __name__=="__main__":
    Main()
