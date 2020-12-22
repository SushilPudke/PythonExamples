# Count no of vowels and Consonents in a String
my_str="axiom techguru pvt. ltd."
vc=0
cc=0

for ch in my_str:
    if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u':
        vc+=1
    else:
        cc+=1

print("No of vowels",vc,"No of consonents ",cc)