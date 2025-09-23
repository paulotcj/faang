# https://leetcode.com/problems/min-cost-climbing-stairs/description/

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        total_cost : int = 0

        cost.append(0) # adding this one just for simplicity and easy to loop the array so we don't need to check limits
        i : int = 0
        #----------------------------------------
        while i < len(cost)-1:
            if  cost[i+1] <= cost[i] : 
                i += 1

            total_cost += cost[i] 
            i += 1
        #----------------------------------------

        return total_cost

    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
class Solution_og : 
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0)

        sum_cost : list[int] = [0] * len(cost)

        #----------------------------------------
        for idx , val in enumerate(cost) :
            #-----
            if idx == 0 or idx == 1 :
                sum_cost[idx] = cost[idx]
                continue
            #-----

            sum_cost[idx] = cost[idx] + min( sum_cost[idx-1] , sum_cost[idx-2] )
        #----------------------------------------

        result : int = sum_cost[-1]

        return result
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
cost = [10,15,20]

expected : int = 15

result = sol.minCostClimbingStairs(cost=cost)

print(f'result: {result} - expected : {expected} - is the result correct: {result==expected}')
exit()
print('---------')

sol = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]

expected : int = 6

result = sol.minCostClimbingStairs(cost=cost)

print(f'result: {result} - expected : {expected} - is the result correct: {result==expected}')

print('---------')