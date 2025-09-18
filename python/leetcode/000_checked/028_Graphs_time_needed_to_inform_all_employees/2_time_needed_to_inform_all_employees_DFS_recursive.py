# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

from collections import defaultdict
#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def dfs(self, employee_id : int) -> int :
        if not self.subordinates[employee_id] : return 0 # if no subordinates, there's no time needed to inform - return 0

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

        manager_id : int = employee_id
        max_time : int = 0
        #----------------------------------------
        for subordinate_id in self.subordinates[employee_id] :
            max_time = max( max_time , self.dfs(subordinate_id) )
        #----------------------------------------

        return_val : int = max_time + self.inform_time[employee_id]
        return return_val
    #-------------------------------------------------------------------------     
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        # step 1 - just create and populate an adjacency list
        self.inform_time : list[int] = informTime
        self.subordinates : dict[int, list[int]] = defaultdict(list) # if the key is not present the default value is an empty list

        #----------------------------------------
        for emp_id, mgr_id in enumerate(manager) : 
            if mgr_id == -1 : continue # -1 means no manager, it's the root node
            self.subordinates[mgr_id].append(emp_id)
        #----------------------------------------

        # step 2 - explore the adjacency list DFS style - return the max time to inform
        return_val : int = self.dfs(employee_id=headID)
        return return_val
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]
expected : int = 13
sol = Solution()
result : int = sol.numOfMinutes(n = 8, headID = 4, manager=managers_array, informTime= inform_time_array)

print(f'Result : {result} - expected : {expected} - is the result the same? {result==expected}')