l=[1,2,2,4,4,5,5,7,8,7]
l1 = set()

for i in range(0,len(l)-1):
    d=0
    for j in l[i:]:
        if l[i]==j:
            d=d+1
    if(d==2):
        l1.add(l[i])
print(l1)