# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        n : int = len(cost)
        
        #-----------------------------------
        for i in range(2, n): # range(2, n) since the min cost for the steps 0 and 1 is their very own cost
            cost[i] = cost[i] + min(cost[i - 1], cost[i - 2]) # considering the cost of this step, get the lower cost between the previous steps i-1 and i-2
        #-----------------------------------
            
        return min(cost[n - 1], cost[n - 2]) # as a last 'n' step (with cost of 0), decice which previous 'step' is the lower cost, n-1 or n-2
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