# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n : int = len(cost)

        dp : List[int] = [ cost[0] , cost[1] ]
        
        #-----------------------------------
        for i in range(2, n):
            current : int = cost[i] + min(dp[0] , dp[1])
            dp[0] = dp[1]
            dp[1] = current
        #-----------------------------------
        
    
        return min( dp[0] , dp[1] )
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        """
        :param cost: List[int]
        :return: int
        Approach 2: Optimized Iteration with Bottom-Up
        """
        n = len(cost)
        if n == 0:
            return 0
        if n == 1:
            return cost[0]

        dp = [cost[0], cost[1]]

        for i in range(2, n):
            current = cost[i] + min(dp[0], dp[1])
            dp[0] = dp[1]
            dp[1] = current

        return min(dp[0], dp[1])
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