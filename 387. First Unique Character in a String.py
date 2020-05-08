'''
Time complexity : O(n)
Space complexity: O(n)
'''

import collections

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = collections.Counter(s)
        
        for ind, c in enumerate(s):
            if count[c]==1:
                return ind
        
        return -1