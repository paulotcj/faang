# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n : int = len(cost)
        memo : List[int] = [0] * n
        #-----------------------------------
        for i in range(n):
            if i < 2 : 
                memo[i] = cost[i]
                continue
            
            memo[i] = cost[i] + min( memo[i-1] , memo[i-2] )
        #-----------------------------------
        
        return min( memo[n-1], memo[n-2] )
        
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    # Approach 2: Iteration w/ Bottom Up Approach
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [0] * n

        for i in range(n):
            if i < 2:
                memo[i] = cost[i]
            else:
                memo[i] = cost[i] + min(memo[i - 1], memo[i - 2])

        return min(memo[n - 1], memo[n - 2])
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