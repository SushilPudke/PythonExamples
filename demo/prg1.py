# demonstrating main() funciton in python

def f1():
    print("I am in f1 definition ")
    print(chr(65))

def facto(n):
    f=1
    while n>0:
        f=f*n
        n=n-1

    return f



def main():
    print("I am in main Funtion")
    f1()
    n=5
    print("Factorial of ",n,"==",facto(n))

if __name__=="__main__":
    main()
