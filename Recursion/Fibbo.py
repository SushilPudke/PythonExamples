# Recursive Fibbonoci Series 

def fibbo(ft,st,tt):
    if tt==2:
        return
    else:
        rt=ft+st
        print(" ",rt,end=' ')
        ft=st
        st=rt
    
    tt-=1
    fibbo(ft,st,tt)

def Main():
    ft=int(input("Enter First Term :"))
    st=int(input("Enter Second Term :"))
    tt=int(input("Enter Total Terms :"))
    print(ft," ",st,end=' ')
    fibbo(ft,st,tt)


if __name__=="__main__":
    Main()


