from collections import defaultdict, deque
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list for the graph
        adj_list = defaultdict(list)
        # Create an array to track the in-degree of each course
        in_degree = [0] * numCourses
        
        #---------------------------
        # Build the graph and in-degree array
        for course, prereq in prerequisites:
            adj_list[prereq].append(course)
            in_degree[course] += 1
        #---------------------------
        
        # Initialize a queue with all courses that have in-degree 0
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        count_pop_stack = 0
        
        #---------------------------
        # Process the courses in topological order
        while queue:
            current_course = queue.popleft()
            count_pop_stack += 1

            #---------------------------
            # Reduce the in-degree of neighboring courses
            for dependent_course in adj_list[current_course]:
                in_degree[dependent_course] -= 1
                # If in-degree becomes 0, add it to the queue
                if in_degree[dependent_course] == 0:
                    queue.append(dependent_course)
            #---------------------------
        #---------------------------
        
        # If we visited all courses, return True, otherwise False
        return count_pop_stack == numCourses
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------