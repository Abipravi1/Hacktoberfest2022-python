my_list = [1, 2, 3, 4, 5]

print("The list is : ")

for i in range(0, len(my_list)):
   print(my_list[i])

print("The list after reversal is : ")

for i in range(len(my_list)-1, -1, -1):
   print(my_list[i])