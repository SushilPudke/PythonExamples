# Demo DivideByZero

x=0
try:
    y=12/x
except : 
    print("DivideByZero Exception")
else :
    print("Something Else Went Wrong")
finally:
    print(f'value of x:{x} ')
   