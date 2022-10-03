def binary_search(arr, x):
    l = 0
    r = len(arr) - 1
    mid = 0
 
    while l <= r:
        mid = (r + l) 
        if arr[mid] < x:
            l = mid + 1
        elif arr[mid] > x:
            r = mid - 1
        else:
            return mid
    return -1
 
arr = []
n = int(input("Enter the number of elements in array : "))
print("Enter the elements")
for i in range(n):
    arr.append(int(input()))

x = int(input("Enter the element to search in the array : "))


res = binary_search(arr, x)
 
if res != -1:
    print("Element is at index", str(res))
else:
    print("Element is not there in array")
