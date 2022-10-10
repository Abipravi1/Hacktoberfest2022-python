import numpy as np

print("Enter numbers")
arr = list(map(int,input().split()))

#Interquartile Range
data = np.array(arr)
q3, q1 = np.percentile(data, [75 ,25])
iqr = q3 - q1
print("Interquartile Range is %.2f"%(iqr))

#low_outliers_margin
value1 = q1 - 1.5*iqr
#high_outliers_margin
value2 = q3 + 1.5*iqr

#total_no_of_low_and_high_outliers
low_outliers = 0
high_outliers = 0
print(value1)

for i in arr:
    if i < value1:
        low_outliers  += 1
    if i > value2:
        high_outliers += 1

print("Total numbers below low outliers are ", low_outliers)
print("Total numbers below high outliers are ", high_outliers)