# Generate Fibbonoci Series of user defined Terms 

# define fibbo function 
def fibbo(ft,st,tt):
    print(ft ," ",st, end=' ')
    for i in range(3,(tt+1)):
        rt=ft+st
        print(" ",rt,end=' '),
        ft=st
        st=rt

def Main():
    ft=int(input("Enter First Term:"))
    st=int(input("Enter Second Term:"))
    tt=int(input("Enter Total Terms:"))
    fibbo(ft,st,tt)


if __name__=="__main__":
    Main()



