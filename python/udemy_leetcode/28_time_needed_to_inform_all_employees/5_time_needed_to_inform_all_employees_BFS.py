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
            if manager[i] == -1: continue
            subordinates[manager[i]].append(i)
        #---------------------------
        
        # Perform BFS to calculate the total time needed
        queue = deque([(headID, 0)])  # (current_employee, time_taken_to_reach)
        max_time = 0
        
        #---------------------------
        while queue:
            '''the major difference between a DFS and a BFS is that the DFS uses a stack, and the
            the BFS is more like a queue, in other other words, the immediate child nodes of a
            a node are processed first, and the accumulate any other nodes we come across to be
            processed later. '''
            current, time_taken_upstream = queue.popleft() 
            max_time = max(max_time, time_taken_upstream)
            
            for subordinate_id in subordinates[current]:
                manager_inform_time : int = informTime[current]
                queue.append((subordinate_id, time_taken_upstream + manager_inform_time))
        #---------------------------
        
        return max_time
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]

sol = Solution()


print(sol.numOfMinutes(8, 4, managers_array, inform_time_array))


#13