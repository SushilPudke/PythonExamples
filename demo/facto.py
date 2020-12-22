# write a user defined function for factorial 
#  n! = n x n-1 x n-2 ....1
def facto(n): 
    f=1
    while n>0:
        f=f*n
        n=n-1

    return f


def main():
    n=int(input("Enter a no:"))
    print(n,"Factorial =",facto(n))


if __name__=="__main__":
    main()



