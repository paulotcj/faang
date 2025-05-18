# https://leetcode.com/problems/min-cost-climbing-stairs/description/

from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n : int = len(cost)
        self.cost : List[int] = cost
        self.memo : Dict[int, int] = {}
        
        return min( self.min_cost(n-1) , self.min_cost(n-2) )
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def min_cost(self, i : int) -> int:
        if i < 0 : return 0
        if i == 0 or i == 1: return self.cost[i]
        
        if i in self.memo: return self.memo[i]
        
        self.memo[i] = self.cost[i] + min( self.min_cost(i-1), self.min_cost(i-2) )
        
        return self.memo[i]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def minCostClimbingStairs2(self, cost: List[int]) -> int:
        # Get the length of the cost array
        n = len(cost)
        memo = {}
        return min(self.minCost(n - 1, cost, memo), self.minCost(n - 2, cost, memo))
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def minCost(self, i, cost, memo):
        # Base Cases
        if i < 0: return 0
        if i == 0 or i == 1: return cost[i]
        
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(self.minCost(i - 1, cost, memo), self.minCost(i - 2, cost, memo))
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