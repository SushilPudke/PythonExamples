# Generating 10 multiples of given no using recursion

def multi(n,x):
    if x==0:
        return
    else:
        print(n," * ",(11-x)," = ",n*(11-x))
    
    x-=1
    multi(n,x) # recursive call to multi


def Main():
    n=int(input("Enter any no for multiples"))
    multi(n,10)

if __name__=="__main__":
    Main()


