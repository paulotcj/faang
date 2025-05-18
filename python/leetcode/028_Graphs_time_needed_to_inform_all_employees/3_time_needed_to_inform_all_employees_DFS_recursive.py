# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

from typing import List, Dict
from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, num_employees: int, headID : int, manager: List[int], informTime: List[int]) -> int:
        self.inform_time : List[int] = informTime
        self.subordinates : Dict[int, List[int]] = defaultdict(list) # if not key is present an empty list is created
        
        for e_id, m_id in enumerate(manager):
            if m_id == -1: continue
            self.subordinates[m_id].append(e_id) # remember this is a list, so we need to append
            
        return self.dfs(employee_id = headID)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dfs(self, employee_id):
        if not self.subordinates[employee_id]: return 0 # leaf node / employees who are not managers
        
        manager_id = employee_id
        max_time = 0
        #---------------------------
        for subordinate_id in self.subordinates[manager_id]:
            max_time = max( max_time, self.dfs(employee_id=subordinate_id) )
        #---------------------------
        
        time_needed = self.inform_time[manager_id] + max_time
        return time_needed
    #-------------------------------------------------------------------------  
#-------------------------------------------------------------------------

managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]

sol = Solution()


print(sol.numOfMinutes(8, 4, managers_array, inform_time_array))


#13