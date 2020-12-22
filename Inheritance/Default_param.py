# Program demonstrate Default,Parameterised Constructor

class Facto:

    
# define default Constructor 
    def __init__(self):
        self.n=3
    
    '''
# Define parameterised constructor
    def __init__(self,n):
        self.n=n
    '''
    def findFacto(self):
        f=1
        while(self.n>0):
            f*=self.n
            self.n-=1
        
        return f
    

def Main():
    #n=int(input("Enter a no:"))
    # f=Facto(n) # call to parameterised constructor
    f=Facto() # call to default constructor 
    print(f'factorial of {f.n}, is {f.findFacto()}')

if __name__=="__main__":
    Main()