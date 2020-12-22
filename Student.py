# A pro for generating Student Mark-sheet 
nm=input("Enter Students Name :")
rn=input("Students Roll No :")
s1=int(input("Enter Marks for Sub1:"))
s2=int(input("Enter Marks for Sub2:"))
s3=int(input("Enter Marks for Sub3:"))
s4=int(input("Enter Marks for Sub4:"))
s5=int(input("Enter Marks for Sub5:"))
# Compute total marks obtained
tot=s1+s2+s3+s4+s5
per=tot/5
# Evaluate Result 
if s1>=40 and s2>=40 and s3>=40 and s4>=40 and s5>=40 and per>=50:
    rslt="Pass"
else:
    rslt="Fail"
#Build condition for Grade 
if per<50 and rslt=="Fail" :
    grade="****"
elif per>=50 and per<65 and rslt=="Pass":
    grade="C"
elif per>=65 and per<75 and rslt=="Pass":
    grade="B"
elif per>=75 and per<85 and rslt=="Pass":
    grade="A"
elif per>=85 and rslt=="Pass":
    grade="A+"
else:
    grade="****"

#print Score Sheet
print("Student Name:",nm,"Roll No ",rn)
print("Sub 1",s1,"Sub 2",s2,"Sub 3",s3,"Sub 4",s4,"Sub 5",s5)
print("Total Marks :",tot,"Percentage ",per)
print("Result ",rslt,"Grade ",grade)




