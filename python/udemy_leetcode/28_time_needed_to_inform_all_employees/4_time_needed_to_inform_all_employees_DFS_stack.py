from typing import List, Dict, Deque
from collections import defaultdict, deque

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, num_employees: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create a dictionary to store subordinates for each manager
        subordinates: Dict[int, List[int]] = defaultdict(list)
        
        #---------------------------
        for e_id, m_id in enumerate(manager):
            if m_id == -1: continue
            subordinates[m_id].append(e_id)
        #---------------------------
        
        # Initialize a stack for iterative DFS
        stack : Deque = deque( [ (headID, 0) ] )  # (current_employee, time_taken_to_reach)
        max_time = 0
        
        # DFS
        #---------------------------
        while stack:
            current_employee_id, current_time = stack.pop()
            max_time = max(max_time, current_time)
            
            # Add all subordinates of the current employee to the stack
            for subordinate in subordinates[current_employee_id]:
                current_employee_inform_time = informTime[current_employee_id]
                stack.append(( subordinate, current_time + current_employee_inform_time ))
        #---------------------------
        
        return max_time
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]

sol = Solution()


print(sol.numOfMinutes(8, 4, managers_array, inform_time_array))


#13