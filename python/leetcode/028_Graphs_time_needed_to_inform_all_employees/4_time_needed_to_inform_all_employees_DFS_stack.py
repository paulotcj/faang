# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

from collections import defaultdict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        # step 1 - just create and populate an adjacency list
        subordinates : dict[int, list[int]] = defaultdict(list)

        #----------------------------------------
        for emp_id , mgr_id in enumerate(manager) :
            if mgr_id == -1 : continue
            subordinates[mgr_id].append(emp_id)
        #----------------------------------------

        # step 2 - explore the adjacency list DFS style - return the max time to inform
        stack : list[list[int]] = [ [headID, 0] ] # head_id starts with 0 inform time from its superiors as it's the head node
        max_time : int = 0
        #----------------------------------------
        while stack : 
            curr_emp_id , time_taken_upstream = stack.pop()
            max_time = max(max_time, time_taken_upstream )

            #----------------------------------------
            # explore child nodes bfs style
            subordinates_slide : list[int] = subordinates[curr_emp_id]
            for subordinate_id in subordinates_slide:
                manager_inform_time : int = informTime[curr_emp_id]
                stack.append( [subordinate_id , manager_inform_time + time_taken_upstream] )
            #----------------------------------------
        #----------------------------------------

        return max_time
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]
expected : int = 13
sol = Solution()
result : int = sol.numOfMinutes(n = 8, headID = 4, manager=managers_array, informTime= inform_time_array)

print(f'Result : {result} - expected : {expected} - is the result the same? {result==expected}')