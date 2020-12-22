# OOP - Student Class 
class Student :

    def __init__(self,name,rn,s1,s2,s3,s4,s5):
        self.name=name
        self.rn=rn
        self.s1=s1
        self.s2=s2
        self.s3=s3
        self.s4=s4
        self.s5=s5

    def compute(self):
        self.tot=self.s1+self.s2+self.s3+self.s4+self.s5
        self.per=float(self.tot/5)

    def display(self):
        print(f"Name {self.name} Roll no {self.rn}")
        print(f" Sub1 :{self.s1},Sub2 :{self.s2},Sub3:{self.s3},Sub4: {self.s4},Sub5:{self.s5} ")
        print(f'Total {self.tot} Percentage{self.per}')


def Main():
    s=Student("Abc",101,67,88,85,76,87)
    s.compute()
    s.display()

if __name__=="__main__":
    Main()
