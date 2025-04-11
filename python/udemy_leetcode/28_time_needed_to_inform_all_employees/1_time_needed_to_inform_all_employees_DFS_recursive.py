
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n, head_id, managers, inform_time):
        subordinates = [[] for _ in range(n)] # creates the adjacency list
        
        #---------------------------
        for employee in range(n):
            manager = managers[employee] # who is the manager of that employee
            
            if manager == -1: # no manager, root node
                continue
            
            subordinates[manager].append(employee) # adjacency list, adds employees IDs under the manager
        #---------------------------
        
        return self.dfs(head_id, subordinates, inform_time)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dfs(self, current_id, adj_list, inform_time):
        if not adj_list[current_id]:
            return 0
        
        max_time = 0
        subordinates = adj_list[current_id]
        for subordinate in subordinates:
            max_time = max(max_time, self.dfs(subordinate, adj_list, inform_time))
        
        return max_time + inform_time[current_id]
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]

sol = Solution()


print(sol.numOfMinutes(8, 4, managers_array, inform_time_array))


# 13