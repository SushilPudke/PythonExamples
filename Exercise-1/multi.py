# Read a no to print 10 multiples of it 

# define a multi function
def multi(n):
    for i in range(1,11):
        print(n," * ",i," = ",(n*i))


# define a Main function
def Main():
    n=int(input("Enter a no"))
    multi(n)



if __name__=="__main__":
    Main()