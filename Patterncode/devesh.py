print('''1. Right-angled triangle

2. Isosceles triangle  
 
3. Kite

4. Half Kite

5. X
''')
op=int(input('Enter the choice')) #enter the triangle u want to print 
n=int(input('enter the number of lines u want to print'))#number of lines you want to print 
if op==1:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end='')
        print()
elif op==2:
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print(' ', end='')
        for  k in range(1,2*i):
            print(k, end='')
        print()
elif op==3:
    for i in range(1,n+1):
        for j in range(0,n-i+1):
            print(' ', end='')
        for  k in range(1,2*i):
            print(k, end='')
        print()
    for i in range(n-1,0,-1):
        for j in range(0,n-i+1):
            print(' ', end='')
        for  k in range(1,2*i):
            print(k, end='')
        print()
elif op==4:
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j, end='')
        print()
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print(j, end='')
        print()
else:
    for i in range(n,0,-1):
        for j in range(0,n-i+1):
            print(' ', end='')
        for  k in range(1,2*i):
            print(k, end='')
        print()
    for i in range(2,n+1):
        for j in range(0,n-i+1):
            print(' ', end='')
        for  k in range(1,2*i):
            print(k, end='')
        print()
