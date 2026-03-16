# Bubble Sort for array of random numbers
import random
#intialize array
array = random.sample(range(1,100),30) # select 30 numbers from a range of 100
temp_variable =0

#print the orginal non sorted array
print ("Elements of the array: ", array)

#sort the array in ascendind order
for i in range(0, len(array)):
 for j in range(i+1, len(array)):
   if (array[i] > array[j]):
     temp_variable = array[i]
     array[i] = array[j]
     array[j] = temp_variable

print()

print("Sorted array in ascending order: ")
print(array)