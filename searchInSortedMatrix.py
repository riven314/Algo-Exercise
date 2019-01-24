# Method1: zigzag method
# Time complexity: O(M+N)
# Space complexity: O(1)

def searchInSortedMatrix(matrix, target):
	current_i, current_j = 0, len(matrix[0])-1
	while current_i < len(matrix) and current_j >=0:
		# shift leftwards if target is smaller
		if target < matrix[current_i][current_j]:
			current_j -= 1
		# shift downwards if target is bigger
		elif target > matrix[current_i][current_j]:
			current_i += 1i
		# The case when target = current value
		else:
			return [current_i, current_j]
	return [-1, -1]
	

