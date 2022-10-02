#Program to check weather a number is palindromic

number = input("enter a number: ")


#the below code finds the number of digits in the number entered
n = 0
for i in number:
    n = n + 1

#the below code reverses the number
rev_number = ""
for a in range (n-1, -1, -1):
    rev_num = number[a]
    rev_number = rev_number + rev_num

#the number is converted to an integer, it was an string before
number = int(number)
rev_number = int(rev_number)

#comparing if the number and its reversed number is equal or not
#and printing the result

if number == rev_number:
    print("the number is a palindrome")
else:
    print("the number is not an palindrome")   