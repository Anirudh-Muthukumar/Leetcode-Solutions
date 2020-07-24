import heapq, collections, random

class Solution:
    def findKthLargest(self, A, k):
        def heapSort():
            n = len(A)
            if k==n:
                return A
            A.sort()
            return A[n-k]
        
        def quickSelection():
            def partition(left, right, pivot_index):
                pivot = A[pivot_index]
                A[pivot_index], A[right] = A[right], A[pivot_index]
                store_index = left
                for i in range(left, right):
                    if A[i] < pivot:
                        A[store_index], A[i] = A[i], A[store_index]
                        store_index += 1
                A[right], A[store_index] = A[store_index], A[right]
                return store_index
            
            def quickSelect(left, right, k_smallest):
                if left==right:
                    return A[left]
                pivot_index = random.randint(left, right)
                pivot_index = partition(left, right, pivot_index)
                if k_smallest == pivot_index:
                    return A[k_smallest]
                elif k_smallest < pivot_index:
                    return quickSelect(left, pivot_index-1, k_smallest)
                else:
                    return quickSelect(pivot_index+1, right, k_smallest)
                
            n = len(A)
            return quickSelect(0, n-1, n-k)
        
        return quickSelection()
        return heapSort()
        