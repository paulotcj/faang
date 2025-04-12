from typing import List, Dict, Deque, Tuple
from collections import defaultdict, deque

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def numOfMinutes(self, num_employees : int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subordinates : Dict[int, List[int]] = defaultdict(list) # Create a dictionary to store subordinates for each manager
        
        #---------------------------
        for e_id, m_id in enumerate(manager):
            if m_id == -1 : continue
            subordinates[m_id].append(e_id)
        #---------------------------
        
        #   (current_employee, time_taken_to_reach) - we know headID will take longer, but this will be sorted out below
        stack : Deque[Tuple[int,int]] = deque( [ (headID, 0) ] ) 
        max_time = 0 # so far that's all we know
        
        #---------------------------
        while stack:
            emp_id, time_upstream = stack.pop()
            max_time : int = max( max_time, time_upstream )
            
            #---------------------------
            subordinates_sublist : List[int] = subordinates[emp_id]
            for subordinate_id in subordinates_sublist:
                manager_inform_time : int = informTime[emp_id]
                
                stack.append( (subordinate_id, manager_inform_time + time_upstream) )
            #---------------------------   
            
        #---------------------------
        
        return max_time    
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def numOfMinutes2(self, num_employees: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        # Create a dictionary to store subordinates for each manager
        subordinates: Dict[int, List[int]] = defaultdict(list)
        
        #---------------------------
        for e_id, m_id in enumerate(manager):
            if m_id == -1: continue
            subordinates[m_id].append(e_id)
        #---------------------------
        # Initialize a stack for iterative DFS
        stack : Deque = deque( [ (headID, 0) ] )  # (current_employee, time_taken_to_reach)
        max_time_so_far = 0
        
        # DFS
        #---------------------------
        while stack:
            current_employee_id, time_taken_upstream = stack.pop()
            max_time_so_far = max(max_time_so_far, time_taken_upstream)
            
            #---------------------------
            # Add all subordinates of the current employee to the stack
            subordinates_current_employee = subordinates[current_employee_id]
            for subordinate_id in subordinates_current_employee:
                
                # we push down to the current employee their manager's inform time so it can all 
                #  be added up. Or in other words, time is only used when the information is passed
                #  the root node does not consume time because it already knows, but it needs time
                #  to comunicate down.
                manager_inform_time = informTime[current_employee_id]
                
                stack.append(( subordinate_id, time_taken_upstream + manager_inform_time ))
            #---------------------------
        #---------------------------
        
        return max_time_so_far
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


managers_array    = [2, 2, 4, 6, -1, 4, 4, 5]
inform_time_array = [0, 0, 4, 0, 7, 3, 6, 0]

sol = Solution()


print(sol.numOfMinutes(8, 4, managers_array, inform_time_array))


#13