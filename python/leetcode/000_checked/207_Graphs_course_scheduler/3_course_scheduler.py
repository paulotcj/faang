# https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict, deque

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list : dict[int, list[int]] = defaultdict(list)
        in_degree : list[int] = [0] * numCourses

        #----------------------------------------
        for dependent_course , prerequisite_course in prerequisites : 
            in_degree[dependent_course] += 1 # number of requirements pointing to that course
            adj_list[prerequisite_course].append(dependent_course) # if I take this course, which couses can I take after this then?
        #----------------------------------------

        queue : deque[int] = deque(
            [
                in_deg_course
                for in_deg_course , in_deg_val in enumerate(in_degree)
                if in_deg_val == 0
            ]
        )

        visited : int = 0 # we need this to detect cyclic blocked courses

        #----------------------------------------
        while queue : 
            zero_in_deg_course : int = queue.popleft()
            visited += 1
            #----------------------------------------
            for dependent_course in adj_list[zero_in_deg_course] :
                in_degree[dependent_course] -= 1
                if in_degree[dependent_course] == 0 : queue.append(dependent_course)
            #----------------------------------------
        #----------------------------------------

        # now it's possible that we have cyclic courses (blocked courses) remaining. We don't need
        #  to list them, but it's enough as the question asks us to be able to tell if we can 
        #  take all the courses or not. And in this case we only can take them all if the number
        #  of courses poped out from the stack is the same as the total number of courses.
        result : bool = visited == numCourses

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