# Apply iterative and recursive method
# Time complexity = O(2**N * N)
# Space complexity = O(2**N * N)

def powerset_iter(array):
	# For storing all subsets
	subset_list = [[]]
	for num in array:
		# For storing subsets containing num
		new_subsets = []
		for subset in subset_list:
			new_subset = subset + [num]
			new_subsets.append(new_subset)
			#print(new_subsets)
		subset_list += new_subsets
	subset_list = sorted(subset_list, key = len)
	return subset_list

def powerset_recur(array, idx = None):
	if idx is None:
		idx = len(array) - 1
	if idx < 0:
		return [[]]
	current_num = array[idx]
	# subsets for array without current_num
	sub_subsets = powerset_recur(array, idx - 1)
	# subsets with current_num appended
	total_subsets = [subset + [current_num] for subset in sub_subsets]
	# combine the two subsets
	total_subsets += sub_subsets
	# sorted the subset list
	total_subsets = sorted(total_subsets, key = len)
	return total_subsets
