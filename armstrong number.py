#progrto find whether the no. is palindrome or not
n=int(input())
k=n
m=n
d=0
s=0
while (k>0):
    r1= k%10
    d=d+1
    k= k//10
while(n>0):
    r2= n%10
    s=s+(r2)**d
    n=n//10
if (s==m):
    print("  armstrong number ")
else:
    print("not an armstrong number")
