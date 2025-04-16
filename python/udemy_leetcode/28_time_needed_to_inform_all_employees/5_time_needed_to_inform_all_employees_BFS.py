from collections import defaultdict, deque
from typing import List, Deque, Tuple, Dict


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates : Dict[int, List[int]] = defaultdict(list)

        #---------------------------
        for employee_id in range(n):
            emp_manager : int = manager[employee_id]
            if emp_manager == -1: continue

            subordinates[emp_manager].append( employee_id )
        #---------------------------

        queue : Deque[Tuple[int,int]] = deque([(headID, 0)])
        max_time : int = 0
        
        #---------------------------
        while queue:
            current_emp_id , time_taken_upstream = queue.pop()
            max_time : int = max(max_time, time_taken_upstream)
            
            #---------------------------
            #explore child nodes BFS style
            subordinates_slice : List[int] = subordinates[current_emp_id]
            for subordinate_id in subordinates_slice:
                manager_inform_time  : int = informTime[current_emp_id]
                
                queue.append( (subordinate_id, manager_inform_time + time_taken_upstream) )
            #---------------------------
                
        #---------------------------
        
        return max_time
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def numOfMinutes_old(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Build an adjacency list to represent the tree structure
        subordinates = defaultdict(list)
        
        #---------------------------
        for employee_id in range(n):
            if manager[employee_id] == -1: continue
            subordinates[manager[employee_id]].append(employee_id)
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

#                    0  1  2  3   4  5  6  7
managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]

sol = Solution()


print(sol.numOfMinutes(8, 4, managers_array, inform_time_array))


#13