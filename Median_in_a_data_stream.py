# Python code for finding the median in a running data stream

import math
from heapq import heappush, heappop, heapify

#Function that finds the median of the data stream
def median(arr, N):
	
	# Declaring two min heaps
	h1 = []
	h2 = []
	for i in range(len(arr)):
	
		# Negation for treating it as max heap
		heappush(h2, -arr[i])
		heappush(h1, -heappop(h2))
		if len(h1) > len(h2):
			heappush(h2, -heappop(h1))

		if len(h1) != len(h2):
			print(-h2[0])
		else:
			print((h1[0] - h2[0])/2)


# Driver code
if __name__ == '__main__':
	arr = list(map(int, input().split()))
	n=len(arr);
	
	# Function call
	median(arr, n)
