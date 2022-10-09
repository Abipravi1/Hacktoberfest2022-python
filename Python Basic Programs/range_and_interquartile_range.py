import numpy as np

print("Enter numbers")
arr = list(map(int,input().split()))

#range
range = max(arr) - min(arr)
print("Range is", range)

#Interquartile Range
data = np.array(arr)
q3, q1 = np.percentile(data, [75 ,25])
iqr = q3 - q1
print("Interquartile Range is %.2f"%(iqr))