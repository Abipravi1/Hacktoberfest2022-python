#sort in ascending

#Sort number in ascending order
print("**** Sorting in ascending order ****")

number = []
n = int(input("Enter the number of elements to be present in integer array : "))

for i in range(0,n):
    digits=int(input())
    number.append(digits)

number.sort()

print("The numbers are sorted in ascending order ",number)

#Sort decimal number in ascending order
decimal = []
d = int(input("Enter the number of elements to be present in decimal array : "))

for i in range(0,d):
    ele = float(input())
    decimal.append(ele)

decimal.sort()

print("The decimal numbers are sorted in ascending order ",decimal)

#Sort String in ascending order
sentence = []
s = int(input("Enter the number of elements to be present in string array : "))

for i in range(0,d):
    ele = input()
    sentence.append(ele)

sentence.sort()

print("The string is sorted in ascending order ",sentence)


#sort in descending
print("**** Sorting in descending order ****")

#Sort number in descending order
number = []
n = int(input("Enter the number of elements to be present in integer array : "))

for i in range(0,d):
    ele = int(input())
    number.append(ele)

number.sort(reverse=True)

print("The numbers are sorted in descending order ",number)

#Sort decimal number in descending order
decimal = []

d = int(input("Enter the number of elements to be present in decimal array : "))

for i in range(0,d):
    ele = float(input())
    decimal.append(ele)

decimal.sort(reverse=True)

print("The decimal numbers are sorted in descending order ",decimal)

#Sort String in descending order
sentence = []
s = int(input("Enter the number of elements to be present in string array : "))

for i in range(0,d):
    ele = (input())
    sentence.append(ele)

sentence.sort(reverse=True)

print("The string is sorted in descending order ",sentence)