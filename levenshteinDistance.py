# Edit distance with dynamic programming
# Time complexity: O(MN), M=length of str1, N=length of str2
# Space complexity: O(MN)

def levenshteinDistance(str1, str2):
	if len(str1)==0 or len(str2)==0:
		return max(len(str1), len(str2))
	# vertical str1, horizontal str2
	edit_table = [[j for j in range(len(str2)+1)] for i in range(len(str1)+1)]
	# fill table vertically
	for i in range(len(str1)+1):
		edit_table[i][0] = i
	# for i in range(1, len(str1)+1):
		for j in range(1, len(str2)+1):
			if str1[i-1] == str2[j-1]:
				edit_table[i][j] = edit_table[i-1][j-1]
			else:
				edit_table[i][j] = min(edit_table[i-1][j], edit_table[i][j-1], edit_table[i-1][j-1])+1
	return edit_table[-1][-1]
