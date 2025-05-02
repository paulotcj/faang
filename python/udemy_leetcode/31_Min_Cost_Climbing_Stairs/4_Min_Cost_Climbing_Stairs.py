# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        self.cost = cost
        
        #final condition of the step N. From here the real lifting is done by min_cost
        return min( self.min_cost(n-1) , self.min_cost(n-2) )
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def min_cost(self,i : int):
        if i < 0 : return 0
        if i == 0 or i == 1: return cost[i]
        
        return cost[i] + min( self.min_cost(i-1) , self.min_cost(i-2) )
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        
        # Get the length of the cost array
        n = len(cost)
        self.cost = cost
        
        return min(self.minCost(n - 1), self.minCost(n - 2))
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def minCost(self, i):
        # Base Cases
        if i < 0: return 0
        if i == 0 or i == 1: return self.cost[i]

        return self.cost[i] + min(self.minCost(i - 1), self.minCost(i - 2))
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