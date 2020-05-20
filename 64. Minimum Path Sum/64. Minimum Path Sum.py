'''
    Time complexity : O(mn)
    Space complexity: O(mn)
'''

def minPathSum(grid):
    m, n = len(grid), len(grid[0])

    # Top Down approach
    def topDown(grid, m, n):

        if m==0 and n==0:
            return grid[m][n]

        if m==0:
            return topDown(grid, m, n-1) + grid[0][n] 

        if n==0:
            return topDown(grid, m-1, n) + grid[m][0]
        
        return min(topDown(grid, m-1, n), topDown(grid, m, n-1)) + grid[m][n]

    # return topDown(grid, m-1, n-1)

    # Bottom Up approach
    cost = []

    for row in grid:
        cost.append(row[:])

    for i in range(1, m):
        cost[i][0] += cost[i-1][0]
    
    for j in range(1, n):
        cost[0][j] += cost[0][j-1]

    for i in range(1, m):
        for j in range(1, n):
            cost[i][j] = min(cost[i-1][j], cost[i][j-1]) + grid[i][j]

    return cost[m-1][n-1]

if __name__ == '__main__':

    maze = [
            [1,3,1],
            [1,5,1],
            [4,2,1]
           ]
    
    print("\nMinimum Path Sum = %d\n" % minPathSum(maze))