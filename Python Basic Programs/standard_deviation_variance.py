print("Enter numbers")
arr = list(map(int,input().split()))

mean = sum(arr)/len(arr)
print("mean is %.1f" % (mean))

sum = 0
for i in arr:
    sum += (i-mean)**2
deviation = sum / len(arr)

print("Standard Deviation is %.2f"%(deviation))

variance = deviation**1/2
print("variance is %.2f"%(variance))
