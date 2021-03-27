n= input("enter the string")
d=0
e=0
x=0
h=0
for i in n:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        d=d +1
    elif(i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        d=d+1
    elif(i>='a' and i<='z'):
        e=e+1
    elif(i>='A' and i<='Z'):
        e=e+1
    elif(i>='0' and i<='9'):
        h= h+1
    else :
        x=x+1
print("the no. of vowels = ",d)
print("the no. of consonants = ",e)
print("the no. of digits = ",h)
print("the no. of  special characters = ",x)







      
