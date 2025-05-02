# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(cost):
        # Get the length of the cost array
        n = len(cost)
        memo = {}
        return min(minCost(n - 1, cost, memo), minCost(n - 2, cost, memo))
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def minCost(i, cost, memo):
        # Base Cases
        if i < 0:
            return 0
        if i == 0 or i == 1:
            return cost[i]
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(minCost(i - 1, cost, memo), minCost(i - 2, cost, memo))
        return memo[i]
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



sol = Solution()

# cost = [10,15,20]

# result = sol.minCostClimbingStairs(cost=cost)

# print(f'result: {result}')
# print('-----------------------------------')

cost = [1,100,1,1,1,100,1,1,100,1]

result = sol.minCostClimbingStairs(cost=cost)

print(f'result: {result}')