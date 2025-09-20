# https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict, deque

#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list : defaultdict[int, list[int]] = defaultdict(list)
        in_degree : list[int] = [0] * numCourses

        #----------------------------------------
        for dependent_course , prerequisite_course in prerequisites:
            in_degree[dependent_course] += 1 # if something points to it, then it increases its in-degree, in this case a requirement points to the course
            adj_list[prerequisite_course].append(dependent_course) # if I take this course, which couses can I take after this then?
        #----------------------------------------

        # let's find where to start - get all current nodes with in-degree of 0
        stack : list[int] = [
            in_degree_course
            for in_degree_course , in_degree_val  in enumerate(in_degree)
            if in_degree_val == 0
        ]

        stack_pop_count : int = 0 # we need this to detect cyclic blocked courses

        #----------------------------------------
        while stack : 
            zero_in_deg_course : int = stack.pop()
            stack_pop_count += 1

            #----------------------------------------
            for dependent_course in adj_list[zero_in_deg_course] : # let's check every course that depends on this current one (zero_in_deg_course)
                in_degree[dependent_course] -= 1 
                if in_degree[dependent_course] == 0 : stack.append(dependent_course) # if this couse becomes a 0 in-degree, add to the stack
            #----------------------------------------
        #----------------------------------------

        # now it's possible that we have cyclic courses (blocked courses) remaining. We don't need
        #  to list them, but it's enough as the question asks us to be able to tell if we can 
        #  take all the courses or not. And in this case we only can take them all if the number
        #  of courses poped out from the stack is the same as the total number of courses.
        result : bool = stack_pop_count == num_courses
        return result
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



# [1,0] -> to take course 1 you need to take course 0
# [2,1] -> to take course 2 you need to take course 1
input : list[list[int]] = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
num_courses : int = 6
sol = Solution()
expected = True
result = sol.canFinish(numCourses=num_courses, prerequisites=input)

print(f'result : {result} - expected : {expected} - is the result what was expected : {result==expected}')

print('--------------')


input : list[list[int]] = [[1,0]]
num_courses : int = 2
sol = Solution()
expected = True
result = sol.canFinish(numCourses=num_courses, prerequisites=input)

print(f'result : {result} - expected : {expected} - is the result what was expected : {result==expected}')

print('--------------')


input : list[list[int]] = [[1,0],[0,1]]
num_courses : int = 2
sol = Solution()
expected = False
result = sol.canFinish(numCourses=num_courses, prerequisites=input)

print(f'result : {result} - expected : {expected} - is the result what was expected : {result==expected}')

print('--------------')