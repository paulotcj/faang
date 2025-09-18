# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
from collections import deque, defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int] ) -> int:
        # build the adjacency list: manager -> list of direct subordinates
        subordinates : dict[int, list[int]] = defaultdict(list)

        #----------------------------------------
        for emp_id , mgr_id in enumerate(manager) :
            if mgr_id == -1 : continue 
            subordinates[mgr_id].append(emp_id)
        #----------------------------------------

        # bfs queue: (current_employee, time_to_reach_this_employee)
        queue : deque[ list[int] ] = deque( [ [headID , 0] ])
        max_time : int = 0

        #----------------------------------------
        while queue : 
            curr_emp_id , current_emp_time = queue.popleft()
            # update the maximum time needed so far
            max_time = max( max_time , current_emp_time )

            # now explore all direct subordinates
            #----------------------------------------
            for subordinate_id in subordinates[curr_emp_id] :
                # each subordinate can be informed after current_time + informTime[curr_emp_id] - and
                #   that is (and careful because this can cause a bug) the way we approach this is that
                #   the lower level employees witout subordinates take 0 min to inform, but their
                #   managers require time, so we always append the manager's time
                queue.append( [ subordinate_id , current_emp_time + informTime[curr_emp_id] ] )

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