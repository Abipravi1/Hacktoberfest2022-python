
# program for tower of hanoi

def toh(n , src, dest, aux):
    if n==1:
        print ("Move disk 1 from source",src,"to destination",dest)
        return
    toh(n-1, src, aux, dest)
    print ("Move disk",n,"from source",src,"to destination",dest)
    toh(n-1, aux, dest, src)

print("Enter N: \n")
n = int(input())

toh(n,'A','B','C')# function called