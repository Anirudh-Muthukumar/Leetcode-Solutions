import heapq

class Solution:
    def findKthLargest(self, A, k):
        
        def heapsort():
            A = [-x for x in A]
            heapq.heapify(A)
            for _ in range(k):
                top = heapq.heappop(A)
            return -top

        
        
        def quickSelect(A, k):
            pivot = A[0]
            left = [l for l in A if l < pivot]
            equal = [e for e in A if e == pivot]
            right = [r for r in A if r > pivot]
            if k <= len(right):
                return quickSelect(right, k)
            elif k <= len(right) + len(equal):
                return equal[0]
            else:
                return quickSelect(left, k - len(right) - len(equal))
        
        
        return quickSelect(A, k)
        