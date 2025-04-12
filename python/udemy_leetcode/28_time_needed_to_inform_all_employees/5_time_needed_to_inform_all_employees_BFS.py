from collections import defaultdict, deque
from typing import List


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Build an adjacency list to represent the tree structure
        subordinates = defaultdict(list)
        
        #---------------------------
        for i in range(n):
            if manager[i] != -1:
                subordinates[manager[i]].append(i)
        #---------------------------
        
        # Perform BFS to calculate the total time needed
        queue = deque([(headID, 0)])  # (current_employee, time_taken_to_reach)
        max_time = 0
        
        #---------------------------
        while queue:
            current, time_taken = queue.popleft()
            max_time = max(max_time, time_taken)
            
            for subordinate in subordinates[current]:
                queue.append((subordinate, time_taken + informTime[current]))
        #---------------------------
        
        return max_time
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------