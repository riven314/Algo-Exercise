# Apply heap data struct to speed up runtime
# Time complexity: O(min(M,N)*log(max(M,N))), M=size of arrayOne, N=size of arrayTwo
# Space complexity: O(1)

# Some issues I missed:
# 1. corner case when difference = 0
# 2. I don't need to store every difference
# 3. I thought space complexity = O(M+N)

import heapq

def smallestDifference(arrayOne, arrayTwo):
	# initialize with heap data struct
	heapq.heapify(arrayOne)
	heapq.heapify(arrayTwo)
	# Pop the smaller of two minimum one by one
	prev_diff = float("inf")
	while arrayOne and arrayTwo:
		next_diff = abs(arrayOne[0] - arrayTwo[0])
		# corner case if difference is 0
		if next_diff == 0:
			return [arrayOne[0], arrayTwo[0]]
		# Update the current smallest difference
		if next_diff < prev_diff:
			ans = [arrayOne[0], arrayTwo[0]]
		prev_diff = next_diff
		if arrayOne[0] <= arrayTwo[0]:
			silent = heapq.heappop(arrayOne)
		else:
			silent = heapq.heappop(arrayTwo)
	return ans
