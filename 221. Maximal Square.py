'''
Classic DP problem with space optimization. We need information about just two rows at any instance of time.
Just maintain two rows of information instead of matrix.

Time complexity : O(mn)
Space complexity: O(n)

'''

def maximalSquare(A):
    m = len(A)
    if m==0:
        return 0
    n = len(A[0])
    first = [0 for _ in range(n)]
    second = [0 for _ in range(n)] 
    maxside = 0
    
    for i in range(m):
        for j in range(n):
            second[j] = 1 if A[i][j]=="1" else 0
            if i>0 and j>0 and second[j]==1:
                second[j] = min(first[j], min(second[j-1], first[j-1])) + 1
            if second[j] > maxside:
                maxside = second[j]
        first = second[:]
    
    return maxside * maxside


print(maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))