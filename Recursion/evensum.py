# Recursive function to generate even nos in the range 0-100 and sum them

def evensum(n,sum):
    if n>100:
        print("summation :",sum)
        return
    else:
        print(n)
        sum+=n
    
    n+=2
    evensum(n,sum)


n=0
sum=0
evensum(n,sum)


