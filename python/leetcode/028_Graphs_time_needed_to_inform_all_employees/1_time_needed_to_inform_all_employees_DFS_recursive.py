# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def dfs( self, current_id : int ) -> int :
        if not self.subordinates[current_id] : return 0

        max_time : int = 0
        subordinates : list[int] = self.subordinates[current_id]
        #----------------------------------------
        for subordinate_id in subordinates:
            max_time = max( max_time , self.dfs( current_id=subordinate_id ) )
        #----------------------------------------

        return_val = int = max_time + self.inform_time [current_id]

        return return_val    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------  
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        self.subordinates : list[list[int]] = [
            [] for _ in range(n)
        ] # creates the adjacency list

        self.inform_time : list[int] = informTime

        #----------------------------------------
        for employee_id in range(n) :
            manager_id : int = manager[employee_id] # who is the manager of that employee

            if manager_id == -1 : continue # no manager, root node

            self.subordinates[manager_id].append(employee_id) # adjacency list, adds employees IDs under the manager
        #----------------------------------------
        return_val : int = self.dfs(current_id = headID)
        return return_val
    #-------------------------------------------------------------------------  
          
#-------------------------------------------------------------------------

managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]
expected : int = 13
sol = Solution()
result : int = sol.numOfMinutes(n = 8, headID = 4, manager=managers_array, informTime= inform_time_array)

print(f'Result : {result} - expected : {expected} - is the result the same? {result==expected}')

