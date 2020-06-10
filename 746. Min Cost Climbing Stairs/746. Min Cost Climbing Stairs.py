class Solution:
    def minCostClimbingStairs(self, cost):
        twoStep = cost[0]
        oneStep = cost[1]
        for i in range(2, len(cost)):
            curr = min(oneStep, twoStep) + cost[i]
            twoStep = oneStep
            oneStep = curr
        
        return min(twoStep, oneStep)
        