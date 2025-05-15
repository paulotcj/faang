# https://leetcode.com/problems/course-schedule/description/

# Topological Sort with adjacency list

from typing import List, Dict, Deque, Tuple
from collections import defaultdict, deque

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree : List[int] = [0] * numCourses # initialization - all courses start with in-degree of 0
        adj_list : List[List[int]] = [ [] for _ in range(numCourses) ]

        #---------------------------
        for course, requirement in prerequisites:
            in_degree[course] += 1 # number of requirements pointing to that course
            adj_list[requirement].append( course ) # parent node and its child nodes
        #---------------------------

        # let's find where to start - get all current nodes with in-degree of 0
        stack : List[int] = []
        #---------------------------
        for course , in_deg_val in enumerate(in_degree):
            if in_deg_val == 0: stack.append(course) # you can start with any of these courses
        #---------------------------

        #---------------------------
        count_pop_stack : int = 0
        while stack:
            current_course = stack.pop() # courses with 0 in-degree
            count_pop_stack += 1

            # since we were able to successfully take the 'current_req_course', all courses
            #   that has his as a dependency must reduce their in-degree number by -1
            #---------------------------
            adj_list_slice = adj_list[current_course]
            for dependent_course in adj_list_slice:
                in_degree[dependent_course] -= 1

                # now if this particular course in-degree level was reduced to 0, from this point
                #   onwards this course can be taken (or enrolled)
                if in_degree[dependent_course] == 0:
                    stack.append(dependent_course)
            #---------------------------
        #---------------------------

        # now it's possible that we have cyclic courses (blocked courses) remaining. We don't need
        #  to list them, but it's enough as the question asks us to be able to tell if we can 
        #  take all the courses or not. And in this case we only can take them all if the number
        #  of courses poped out from the stack is the same as the total number of courses.

        return count_pop_stack == numCourses
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def canFinish_old(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree : List[int] = [0] * numCourses
        adj_list : List[List[int]] = [ [] for _ in range(numCourses) ]

        #---------------------------
        for pair in prerequisites:
            course, requirement = pair

            in_degree[course] += 1
            adj_list[requirement].append(course)
        #---------------------------

        stack : List[int] = []
        #---------------------------
        for i in range(len(in_degree)):
            if in_degree[i] == 0: # you can start with any of these courses
                stack.append(i)
        #---------------------------

        count : int = 0
        #---------------------------
        while stack:
            current_req_course : int = stack.pop() # courses with 0 in-degree
            count += 1

            # since we were able to successfully take the 'current_req_course', all courses
            #   that has his as a dependency must reduce their in-degree number by -1
            #---------------------------
            adj_list_slice = adj_list[current_req_course] # we need to complete current before attenting these courses
            for dependent_course in adj_list_slice:
                in_degree[dependent_course] -= 1

                # now if this particular course in-degree level was reduced to 0, from this point
                #   onwards this course can be taken (or enrolled)
                if in_degree[dependent_course] == 0:
                    stack.append(dependent_course)
            #---------------------------
        #---------------------------

        # now it's possible that we have cyclic courses (blocked courses) remaining. We don't need
        #  to list them, but it's enough as the question asks us to be able to tell if we can 
        #  take all the courses or not. And in this case we only can take them all if the number
        #  of courses poped out from the stack is the same as the total number of courses.

        return count == numCourses
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

# [1,0] -> to take course 1 you need to take course 0
# [2,1] -> to take course 2 you need to take course 1
p = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
sol = Solution()

print(sol.canFinish(6, p))