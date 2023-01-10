class Solution:
    def fourSum(self, n: List[int], t: int):
    	if not n: return []
    	n.sort()
    	L, N, S, M = len(n), {j:i for i,j in enumerate(n)}, set(), n[-1]
    	for i in range(L-3):
    		a = n[i]
    		if a + 3*M < t: continue
    		if 4*a > t: break
    		for j in range(i+1,L-2):
    			b = n[j]
    			if a + b + 2*M < t: continue
    			if a + 3*b > t: break
    			for k in range(j+1,L-1):
    				c = n[k]
    				d = t-(a+b+c)
    				if d > M: continue
    				if d < c: break
    				if d in N and N[d] > k: S.add((a,b,c,d))
    	return S
	




	
