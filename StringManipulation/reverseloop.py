# Reversing a String by setting a loop

def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = "Axiom TechGuru"
  
print ("The original string  is : ",end="") 
print (s) 
  
print ("The reversed string(using loops) is : ",end="") 
print (reverse(s)) 