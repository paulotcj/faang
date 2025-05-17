# https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict, deque
from typing import List, DefaultDict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list : DefaultDict[int, List[int]] = defaultdict(list)
        in_degree : List[int] = [0] * numCourses

        #---------------------------
        for course , requirement in prerequisites:
            in_degree[course] += 1 # if something points to it, then it increases its in-degree, in this case a requirement points to the course
            adj_list[requirement].append(course) # this is a classic relation for a graph, the parent node holds a list of all its children
        #---------------------------

        stack : List[int] = [ course 
                             for course, in_deg_val in enumerate(in_degree) 
                             if in_deg_val == 0 ]
        count_stack_pop : int = 0

        #---------------------------
        while stack:
            current_course : int = stack.pop()
            count_stack_pop += 1

            for dependent_course in adj_list[current_course]:
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0 : stack.append(dependent_course)
        #---------------------------

        return count_stack_pop == numCourses
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def canFinish_old(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
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


p = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
sol = Solution()

print(sol.canFinish(6, p))