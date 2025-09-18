# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))
from collections import deque, defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int] ) -> int:
        # Build the adjacency list: manager -> list of direct subordinates
        subordinates: dict[int, list[int]] = defaultdict(list)
        #----------------------------------------
        for employee_id, mgr_id in enumerate(manager):
            if mgr_id != -1:
                subordinates[mgr_id].append(employee_id)
        #----------------------------------------
        
        # BFS queue: (current_employee, time_to_reach_this_employee)
        queue: deque[tuple[int, int]] = deque()
        queue.append((headID, 0))
        
        max_time: int = 0
        
        #----------------------------------------
        while queue:
            current_id, current_time = queue.popleft()
            # Update the maximum time needed so far
            max_time = max(max_time, current_time)
            # Traverse all direct subordinates

            #----------------------------------------
            for subordinate in subordinates.get(current_id, []):
                # Each subordinate can be informed after current_time + informTime[current_id]
                queue.append((subordinate, current_time + informTime[current_id]))
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