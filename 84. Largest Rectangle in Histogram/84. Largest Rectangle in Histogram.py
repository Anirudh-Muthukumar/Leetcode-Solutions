"""
Idea: Mono stack and use of NLE/PLE

Time complexity: O(n)
Space complexity: O(n)
"""

import collections

class Solution:
    def largestRectangleArea(self, A):
        n = len(A)
        left = [i+1 for i in range(n)]
        right = [n-i for i in range(n)]
        
        st = collections.deque()
        for i in range(n):
            while st and A[st[-1]] > A[i]:
                st.pop()
            
            left[i] = i-st[-1] if st else i + 1
            st += i,
        
        st = collections.deque()
        for i in range(n):
            while st and A[st[-1]] > A[i]:
                right[st[-1]] = i - st[-1]
                st.pop()
            
            st += i,
            
        res = float('-inf')
        for i in range(n):
            res = max(res, A[i] * (left[i] + right[i] - 1))
        
        return res