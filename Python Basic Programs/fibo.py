n = int(input("Enter How Many Number Of Fibonachi Serise Do You Want : "))
fibo = lambda x:x if x < 2 else fibo(x-2) + fibo(x-1)
print(list(map(fibo,range(1,n+1))))
