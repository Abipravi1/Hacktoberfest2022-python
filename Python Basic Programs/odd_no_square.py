#Program to print the sum of the following series till the number of terms the user enters
#1^2 + 3^2 + 5^2 + .... + n^2
#eg. if rang = 3, the computer will calculate 1^2 + 3^2 + 5^2
#eg. if rang = 5, the computer will calculate 1^2 + 3^2 + 5^2 + 7^2 + 9^2

#fist we can see that the bases are nothing but odd numbers


#rang is nothing but the number of terms (n)
rang = int(input("enter the range(value of n): "))

i = 0
a = 1

b = 0

while i < rang:
    odd_sq = a ** 2
    b = odd_sq + b

    a = a + 2
    i = i + 1

print(b)       