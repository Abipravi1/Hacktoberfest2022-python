# Sort array/matrix
# Set a temporary variable that iterates over array elements
# Do a swapping between adjacent elements if necessary

import random

# temporary variable ready for swapping
temp = 0

# using random.sample()
# to generate random number list
data = random.sample(range(1, 50), 20)


def swap(temp, x, y):
    temp = y
    y = x
    x = temp


outerIndex = 0

while outerIndex < len(data):
    # Restart innerIndex so that it repeats scanning after doing a round of sorting 
    innerIndex = 0

    # Include outerIndex so that we don't re-scan items already sorted
    while innerIndex in range(len(data) - outerIndex - 1):
        temp = data[innerIndex]

        # Do a swap between adjacent elements
        if (temp > data[innerIndex+1]):
            data[innerIndex], data[innerIndex + 1] = data[innerIndex + 1], data[innerIndex]
        innerIndex += 1
    outerIndex += 1

print("Sorted list",data)
