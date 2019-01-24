# Apply recursion to do permutation
# Time complexity: N!*N^2 
# Space complexity: N!*N

def getPermutations(array):
	permu = []
	permus = []
	if not len(array) == 0:
		recurse_helper(array, permu, permus)
	return permus

def recurse_helper(array, permu, permus):
	if len(array) == 0:
		permus.append(permu)
	else:
		for next_num in array:
			next_array = [i for i in array if i != next_num]
			next_permu = permu + [next_num]
			recurse_helper(next_array, next_permu, permus)
