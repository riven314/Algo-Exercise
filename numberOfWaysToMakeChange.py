# Space complexity = O(N)
# Time complexity = O(N*d) 

def numberOfWaysToMakeChange(n, denoms):
	combo_count = [0 for i in range(n+1)]
	combo_count[0] = 1
	for denom in denoms:
		for amount in range(len(combo_count)):
			if denom <= amount:
				combo_count[amount] = combo_count[amount] + combo_count[amount-denom]
	return combo_count[-1]
