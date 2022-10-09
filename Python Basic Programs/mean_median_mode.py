print("Enter numbers")
arr = list(map(int,input().split()))

#mean
mean = sum(arr)/len(arr)
print("mean is %.1f" % (mean))

#median
arr.sort()
mid = int(len(arr)/2) 
if len(arr) % 2 == 0:
    median = (arr[mid] + arr[mid-1]) / 2
else:
    median = arr[mid]
print("median is %.1f" % (median))

#mode
mode = {}
val = []
for i in arr:
    if i not in val:
        val.append(i)

for i in val:
    mode[i]=arr.count(i)

res = True
test_val = list(mode.values())[0]
for ele in mode:
    if mode[ele] != test_val:
        res = False
        break

mode_value = 0
if res == False:
    mode_value = max(mode, key= lambda x: mode[x])

if mode_value != 0:
    print("Mode is ", mode_value)
else:
    print("No mode")