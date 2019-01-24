# Apply Dynamic Programming
# Time complexity = O(N*2)/ O(N)?
# As outer loop, we iterate over each index of the list
# For each index, we iterate a constant number of time (equal to the value of the index)
# Space complexity = O(N)

def minNumberOfJumps(array):
	min_jump = [float("inf") for i in range(len(array))]
	min_jump[0] = 0
	for idx, incre_jump in enumerate(array):
		for i in range(incre_jump):
			jump_position = idx + i + 1
			# break the inner loop if considered position is beyond array scope
			if jump_position >= len(array):
				break
			min_jump[jump_position] = min(min_jump[idx]+1, min_jump[jump_position])
	return min_jump[-1]
