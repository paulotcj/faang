# https://leetcode.com/problems/time-needed-to-inform-all-employees/description/

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def dfs( self, current_emp_id : int ) -> int :
        curr_subordinates : list[int] = self.subordinates_adj_list[current_emp_id]
        if not curr_subordinates : return 0 # if no subordinates, there's no time needed to inform - return 0

        # now we look at all subordinates to this employee. If its subordinates don't have anyone below
        #   them, then they will return time_required = 0. If they do have anyone underneath them then
        #   they will return the time needed to inform their respective subordinates, going down all the
        #   way in the graph.
        # Some subordinates may need more time to inform than other subordinates, their graph might
        #   be deeper with longer inform times, im that case we need to keep track of max_time
        #   between all direct subordinates from this current_emp_id
        # Eventually the algorithm will receive back the time needed to inform all subordinates of this
        #   current_emp_id, then we need to add the time it takes this current_emp_id to inform the
        #   subordinates
        max_time : int = 0
        #----------------------------------------
        for subordinate_id in curr_subordinates:
            max_time = max( max_time , self.dfs( current_emp_id=subordinate_id ) )
        #----------------------------------------

        return_val : int = max_time + self.inform_time [current_emp_id]

        return return_val    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------  
    def numOfMinutes(self, n: int, headID: int, manager: list[int], informTime: list[int]) -> int:
        # step 1 - just create and populate an adjacency list
        self.subordinates_adj_list : list[list[int]] = [
            [] for _ in range(n)
        ] # creates the adjacency list

        self.inform_time : list[int] = informTime

        #----------------------------------------
        for employee_id in range(n) : # fill in the adjacency list
            manager_id : int = manager[employee_id] # who is the manager of that employee

            if manager_id == -1 : continue # no manager, root node

            self.subordinates_adj_list[manager_id].append(employee_id) # adjacency list, adds employees IDs under the manager
        #----------------------------------------
        # step 2 - explore the adjacency list DFS style - return the max time to inform
        return_val : int = self.dfs(current_emp_id = headID) # now explore the graph, DFS
        return return_val
    #-------------------------------------------------------------------------  
#-------------------------------------------------------------------------

managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]
expected : int = 13
sol = Solution()
result : int = sol.numOfMinutes(n = 8, headID = 4, manager=managers_array, informTime= inform_time_array)

print(f'Result : {result} - expected : {expected} - is the result the same? {result==expected}')

