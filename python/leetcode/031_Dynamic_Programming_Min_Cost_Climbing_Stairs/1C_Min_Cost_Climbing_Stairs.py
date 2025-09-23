# https://leetcode.com/problems/min-cost-climbing-stairs/description/

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        total_cost : int = 0

        cost.append(0) # adding this one just for simplicity and easy to loop the array so we don't need to check limits
        i : int = len(cost)-1
        #----------------------------------------
        while i >= 2 :
            cost_1_step_back : int = cost[i-1] + cost[i]
            cost_2_step_back : int = cost[i-2] + cost[i]
            if cost_1_step_back < cost_2_step_back:
                total_cost += cost[i-1]
                i -= 1
            else: 
                total_cost += cost[i-2]
                i -= 2
        #----------------------------------------

        return total_cost
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

[10,15,20,0]
[0,2,2,1,0]

[0,2,2,1]

sol = Solution()
cost = [0,2,2,1]

expected : int = 2

result = sol.minCostClimbingStairs(cost=cost)

print(f'result: {result} - expected : {expected} - is the result correct: {result==expected}')
exit()
print('---------')


# sol = Solution()
# cost = [10,15,20]

# expected : int = 15

# result = sol.minCostClimbingStairs(cost=cost)

# print(f'result: {result} - expected : {expected} - is the result correct: {result==expected}')
# exit()
# print('---------')

sol = Solution()
cost = [1,100,1,1,1,100,1,1,100,1]

expected : int = 6

result = sol.minCostClimbingStairs(cost=cost)

print(f'result: {result} - expected : {expected} - is the result correct: {result==expected}')

print('---------')