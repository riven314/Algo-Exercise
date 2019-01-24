# Space Complexity = O(N), where N = total amount 
# Time Complexity = O(N*d), where d = number of denoms

def minNumberOfCoinsForChange(n, denoms):
	minCoins = [float("inf") for i in range(n+1)]
	minCoins[0] = 0
	for denom in denoms:
		for amount in range(len(minCoins)):
			if denom <= amount:
				minCoins[amount] = min(minCoins[amount], 1+minCoins[amount-denom])
	if minCoins[-1] == float("inf"):
		ans = -1
	else:
		ans = minCoins[-1]
	return ans

if __name__ == "__main__":
	n = 7
	denoms = [1,2,5]
	ans = minNumberOfCoinsForChange(n, denoms)
	print('Denoms=%s/n=%d/ans=%d' % (str(denoms), n, ans))
	
