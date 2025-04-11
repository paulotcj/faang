
from typing import List, Dict
from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Build an adjacency list to represent the tree structure
        self.informTime : List[int] = informTime
        self.subordinates: Dict[int, List[int]] = defaultdict(list)
        
        #---------------------------
        for employee, mgr in enumerate(manager):
            if mgr != -1:
                self.subordinates[mgr].append(employee)
        #---------------------------
        
        # Start DFS from the head of the company
        return self.dfs(headID)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    # DFS function to calculate the time to inform all subordinates
    def dfs(self, employee: int) -> int:
        if not self.subordinates[employee]:  # If no subordinates, return 0
            return 0
        
        max_time = 0
        #---------------------------
        for subordinate in self.subordinates[employee]:
            max_time = max(max_time, self.dfs(subordinate))
        #---------------------------
        return self.informTime[employee] + max_time
    #-------------------------------------------------------------------------    
#-------------------------------------------------------------------------

managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]

sol = Solution()


print(sol.numOfMinutes(8, 4, managers_array, inform_time_array))


#13