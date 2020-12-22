# Demo Static data , Methods in Python

class Bank:
    Bbal=0
    def __init__(self,dname,acn,amt):
        self.dname=dname
        self.acn=acn
        self.amt=amt
        Bank.Bbal+=self.amt

    def display(self):
        print(f'Depositor Name:{self.dname},Account No:{self.acn},Amount Balace:{self.amt}')

    def deposite(self,damt):
        print(f'amount Deposited:{damt}')
        self.amt+=damt
        Bank.Bbal+=damt
    def withdraw(self,wamt):
        print(f'amount to Withdraw:{wamt}')
        if self.amt>wamt:
            self.amt-=wamt
        else:
            print("Insufficient Balance")
        Bank.Bbal-=wamt    
    # Static method defined
    def bankbal():
        print(f'Bank Balance:{Bank.Bbal}')


def Main():
    Bank.bankbal()
    d1=Bank("Abc",100,5000)
    d2=Bank("Pqr",200,10000)
    d3=Bank("Lmn",300,8000)
    
    # Display individual Account Details
    d1.display()
    d2.display()
    d3.display()
    # Display total Bank Balance
    Bank.bankbal()
    d1.deposite(3000)
    d1.display()
    Bank.bankbal()
    d2.withdraw(4000)
    d2.display()
    Bank.bankbal()
    d3.deposite(6000)
    d3.display()
    Bank.bankbal()

if __name__=="__main__":
    Main()
