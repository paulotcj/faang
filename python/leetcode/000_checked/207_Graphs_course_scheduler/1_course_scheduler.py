# https://leetcode.com/problems/course-schedule/description/

# Topological Sort with adjacency list


from collections import defaultdict, deque

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        adj_list : list[list[int]] = [ [] for _ in range(numCourses) ]
        in_degree : list[int] = [0] * numCourses # initialization - all courses start with in-degree of 0

        #----------------------------------------
        for dependent_course , prerequisite_course in prerequisites :
            in_degree[dependent_course] += 1 # number of requirements pointing to that course

            # this detail is a little bit confusing, as in should the adj list key be the dependent_course or the prerequisite_course?
            #   and the answer is that the use case is: we want to use a list to lookup and think: if I take this course which
            #   other course can I take? so then prerequisite_course is the key and the dependent_course is the value appended to the list
            adj_list[prerequisite_course].append(dependent_course) # parent node and its child nodes
        #----------------------------------------

        # let's find where to start - get all current nodes with in-degree of 0
        stack : list[int] = []
        #----------------------------------------
        for course , in_deg_val in enumerate(in_degree) :
            if in_deg_val == 0 : stack.append(course) # you can start with any of these courses
        #----------------------------------------

        count_pop_stack : int = 0
        #----------------------------------------
        while stack : 
            current_course : int = stack.pop()
            count_pop_stack += 1

            # since we were able to successfully take the 'current_req_course', all courses
            #   that has his as a dependency must reduce their in-degree number by -1
            #----------------------------------------
            for dependent_course in adj_list[current_course] : # quick tip: this will loop throughout the list of dependent courses 
                in_degree[dependent_course] -= 1

                # now if this particular course in-degree level was reduced to 0, from this point
                #   onwards this course can be taken (or enrolled)
                if in_degree[dependent_course] == 0 :
                    stack.append(dependent_course)                
            #----------------------------------------
                        
        #----------------------------------------

        # now it's possible that we have cyclic courses (blocked courses) remaining. We don't need
        #  to list them, but it's enough as the question asks us to be able to tell if we can 
        #  take all the courses or not. And in this case we only can take them all if the number
        #  of courses poped out from the stack is the same as the total number of courses.
        return count_pop_stack == numCourses  


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