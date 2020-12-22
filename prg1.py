# Read any 3 nos to find greatest and lowest among them 
a=int(input("Enter First No"))
b=int(input("Enter Second No"))
c=int(input("Enter Third no"))

# Logic to determine greatest 
if a>b and a>c :
    print(a,"is greatest")
elif b>a and b>c:
    print(b,"is greatest")
else:
    print(c,"is greatest")
    
# Logic to determine Lowest 
if a<b and a<c :
    print(a,"is Lowest")
elif b<a and b<c:
    print(b,"is Lowest")
else:
    print(c,"is Lowest")
