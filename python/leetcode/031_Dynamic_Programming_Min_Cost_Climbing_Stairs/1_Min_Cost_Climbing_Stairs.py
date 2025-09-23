# https://leetcode.com/problems/min-cost-climbing-stairs/description/

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cost.append(0) # just to make it easier

        sum_cost : list[int] = [0] * len(cost)

        ''' the basic idea in this approach is to look back as opposed to look ahead. Looking
        ahead will not work in certain situations such as [10,15,20], where if you were to
        use a greedy approach and pick the smallest step, you would pick 10, but the answer
        to this problem can only be found if the end is considered.
        We need to use dynamic programming to solve this problem.
         '''

        #----------------------------------------
        for idx , val in enumerate(cost) :
            #-----
            if idx == 0 or idx == 1 : # if you are at idx 0 or 1 you don't have 2 steps back to look, so use their own cost
                sum_cost[idx] = cost[idx]
                continue
            #-----
            min_cost : int = min( sum_cost[idx-1] , sum_cost[idx-2] )
            sum_cost[idx] = cost[idx] + min_cost
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