# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        cost.append(0)
        
        sum_cost : List[int] = [0] * len(cost)
        
        #-----------------------------------
        for idx, val in enumerate(cost):
            if idx == 0 or idx == 1 : 
                sum_cost[idx] = cost[idx]
                continue
            
            sum_cost[idx] = cost[idx] + min(sum_cost[idx-1], sum_cost[idx-2])
        #-----------------------------------
        
        result = sum_cost[-1]
        
        return result
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