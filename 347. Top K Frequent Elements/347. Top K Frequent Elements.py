import collections
import heapq

class Solution:
    def topKFrequent(self, nums, k):
        if k==len(nums): # handling (NlogN) case
            return nums
        A = collections.Counter(nums)
        return heapq.nlargest(k, A, key = A.get)