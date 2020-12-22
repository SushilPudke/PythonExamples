# user defined function to read a no and find factorial

def facto(n):
    f=1
    while(n>0):
        f*=n
        n-=1
    return f

#define Main
def Main():
    n=int(input("Enter a no:"))
    print(n,"Factorial ",facto(n))


# declaration of main
if __name__=="__main__":
    Main()
