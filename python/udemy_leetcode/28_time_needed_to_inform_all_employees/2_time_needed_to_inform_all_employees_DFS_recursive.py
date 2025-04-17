# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/


from typing import List, Dict
from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, num_employees: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.inform_time : List[int] = informTime
        self.subordinates: Dict[int, List[int]] = defaultdict(list) # if the key is not present the default value is an empty list
        
        #---------------------------
        for employee_id, mgr_id in enumerate(manager): # let's build the adjacency list
            if mgr_id == -1: continue # -1 equals no manager, it's the root node
            self.subordinates[mgr_id].append(employee_id)
        #---------------------------
        
        # Start DFS from the head of the company
        return self.dfs(employee_id = headID) #at this point the adjency list self.subordinates is read to be processed
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    # DFS function to calculate the time to inform all subordinates
    def dfs(self, employee_id: int) -> int:
        if not self.subordinates[employee_id]: return 0 # leaf node / employees who are not managers
        
        ''' the logic below is that having an employee ID we will set the time to 0 and we will 
          explore down the tree DFS style. 
          When we reach the leaf node, or an employee without subordinates, we return its inform 
          time, which is 0. 
          Then when this bubble up back to its manager. The lowest manager having explored all 
          its leaf subordinates, will inform its own report time (x1) and their reports (0), to 
          its upper management.
          The upper management will receive the report time from manager x1 (and potentially 
          from other lower managers too), add its own time and bubble up as many levels as 
          necessary until the answer is achieved'''
        
        manager_id = employee_id
        max_time = 0
        #---------------------------
        for subordinate in self.subordinates[manager_id]:
            max_time = max(max_time, self.dfs(subordinate))
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