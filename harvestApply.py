
import heapq

def getDisjointMax(apples, K, L):
	# check for corner case
	n = len(apples)
	if K + L > n:
		return -1
	# first select max from K steps
	max_info = getMaxInfo(apples, K)
	# create a priority queue for all L-step harvest case appended with neg
	l_arr = harvestArr(apples, L)
	maxs = []
	for k_i, k_sum in max_info:
		l_i, l_sum = heapq.heappop(l_arr)*-1
		print('%d is picked' % l_sum)
		while l_i in range(k_i-L+1, k_i+K):
			l_i, l_sum = heapq.heappop(l_arr)*-1
			print('%d is picked' % l_sum)
		maxs.append((k_sum + l_sum)*-1)
	heapq.heapify(maxs)
	max = heapq.heappop(maxs)*-1
	return max

# O(N)
def harvestArr(apples, step):
	n = len(apples)
	step_arr = []
	end_pt = n - step + 1
	for i in range(end_pt):
		h_sum = harvest(apples, i, step)
		# mult by negative because extract min
		heapq.heappush(step_arr, (-1*h_sum, i))
	return step_arr

# O(N)
def getMaxInfo(apples, step):
	n = len(apples)
	end_pt = n - step + 2
	max_info = []
	max = -1
	for i, num in enumerate(range(end_pt)):
		h_sum = harvest(apples, i, step)
		if h_sum > max:
			max = h_sum
			max_info = [(i, h_sum)]
		elif h_sum == max:
			max_info.append((i, h_sum))
	return max_info

# O(1)
def harvest(apples, i, step):
	if step == 1:
		return apples[i]
	else:
		h_sum = sum(apples[i:i+step])
		return h_sum
