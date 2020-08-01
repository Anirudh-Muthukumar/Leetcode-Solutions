import collections

class Solution:
    def majorityElement(self, A):
        # Boyer-Moore Voting algorithm generalization for n/k 
        n = len(A)
        k = 3
        counters = collections.defaultdict(int) 
        occurences = collections.defaultdict(int) 
        res = []
        
        for x in A:
            occurences[x] += 1
            
            if len(counters) < k-1 or x in counters:
                if x not in counters:
                    counters[x] = 0
                counters[x] += 1
            else:
                for key in counters:
                    counters[key] -= 1
                counters = {key: val for key, val in counters.items() if val}
        
        for key in counters:
            if occurences[key] > n//k:
                res.append(key)
        
        return res