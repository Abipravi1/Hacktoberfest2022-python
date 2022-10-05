print("Enter the Value of n: ")
n = int(input())
print("Enter " +str(n)+ " Numbers: ")
nums = []
for i in range(n):
    nums.insert(i, int(input()))

sum = 0
for i in range(n):
    sum = sum+nums[i]

avg = sum/n
print("\nAverage = ", avg)