n =int(input())
for i in range(1, n+1):
    if (i==1):
          for k in range (1, n+1-i):
            print(" ",end = ' ' )
          print(" *",end = ' ')
    elif(i==n):
        for j in range(1, 2*i-1):
            print('*', end = ' ' )
            
    else:
        for k in range (1, n+1-i):
            print(" ",end = ' ' )
        print("*",end = ' ' )
        for l in range (1, 2*i-1):
             print(" ",end = ' ' )
        print('*', end = ' ' )
    print()     
