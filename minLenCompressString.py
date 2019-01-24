import heapq

def minLenCprStr(S, K):
	# get compressed str
	cpr_str = CompressStr(S)
	# get array storing frq
	chr_arr, frq_arr = FrqTable(cpr_str)
	# enumerate the frequency table
	min_lens = []
	for i, _ in enumerate(chr_arr):
		min_len = RemoveStr(chr_arr, frq_arr, i, K) 
		min_lens.append(min_len)
	# O(logN)
	heapq.heapify(min_lens)
	g_min_len = heapq.heappop(min_lens)
	return g_min_len

def RemoveStr(chr_arr, frq_arr, i, K):
	edit_frq_arr = frq_arr.copy()
	# edit the frequency table if start remove string at i-th idx
	EditFrqArr(chr_arr, edit_frq_arr, i, K)
	# synthesize result string 
	edit_cpr_str = SynCprStr(chr_arr, edit_frq_arr)
	return len(edit_cpr_str)
	
def EditFrqArr(chr_arr, frq_arr, i, K):
	# edit the frequency table
	if frq_arr[i] > K:
		frq_arr[i] -= K
	elif frq_arr[i] == K:
		frq_arr[i] = 0
	else:
		K -= frq_arr[i]
		frq_arr[i] = 0
		EditFrqArr(chr_arr, frq_arr, i+1, K)

def SynCprStr(chr_arr, frq_arr):
	# Create table for synthesis of string
	fnl_chr_arr, fnl_frq_arr = ['*'], ['*'] 
	for i, c in enumerate(chr_arr):
		if frq_arr[i] == 0:
			continue
		else:
			if fnl_chr_arr[-1] != c:
				fnl_chr_arr.append(c)
				fnl_frq_arr.append(frq_arr[i])
			else:
				fnl_frq_arr[-1] += frq_arr[i]
	# Synthesis string from the above table
	fnl_cpr_str = ''
	for fnl_frq, fnl_c in zip(fnl_frq_arr[1:], fnl_chr_arr[1:]):
		fnl_cpr_str += str(fnl_frq) + str(fnl_c)
	return fnl_cpr_str

def FrqTable(cpr_str):
	frq_arr, chr_arr = [], []
	c_cnt = ''
	for i, c in enumerate(cpr_str):
		if not IsNumber(c):
			c_cnt = int(c_cnt)
			frq_arr.append(c_cnt)
			chr_arr.append(c)
			c_cnt = ''
		else:
			c_cnt += c
	return chr_arr, frq_arr

def IsNumber(character):
	try:
		int(character)
		return True
	except:
		return False

def CompressStr(S):
	cpr_str = ''
	cnt = 1
	for i, c in enumerate(S):
		if i==0:
			continue
		if S[i] == S[i-1]:
			cnt += 1
		else:
			abbr_w = str(cnt) + S[i-1]
			cpr_str += abbr_w
			cnt = 1
	abbr_w = str(cnt) + S[-1]
	cpr_str += abbr_w
	return cpr_str

