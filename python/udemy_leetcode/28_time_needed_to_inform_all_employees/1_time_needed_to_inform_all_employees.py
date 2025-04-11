
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n, head_id, managers, inform_time):
        adj_list = [[] for _ in range(n)]
        
        for employee in range(n):
            manager = managers[employee]
            if manager == -1:
                continue
            adj_list[manager].append(employee)
        
        return self.dfs(head_id, adj_list, inform_time)

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