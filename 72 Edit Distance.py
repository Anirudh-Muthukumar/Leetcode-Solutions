'''
Time Complexity : O(mn)
Space Complexity: O(mn)

'''

def editDistance(X, Y):

    m, n = len(X), len(Y)

    # 2D array to store results of subproblems
    T = [[0 for _ in range(n+1)]for _ in range(m+1)]

    # source is empty and target is non-empty: insertions
    for j in range(1, n+1):
        T[0][j] = j 
    
    # source is non-empty and target is empty: deletions
    for i in range(1, m+1):
        T[i][0] = i 
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1]==Y[j-1]:
                substitutionCost = 0
            else: 
                substitutionCost = 1 

            insertionCost = T[i-1][j]
            deletionCost = T[i][j-1]

            T[i][j] = min(min(insertionCost + 1, deletionCost + 1), T[i-1][j-1] + substitutionCost) 
        
    return T[m][n]


if __name__ == '__main__':
    X = "intention"
    Y = "execution"

    print("Edit distance = ", editDistance(X, Y))