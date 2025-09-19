# https://leetcode.com/problems/course-schedule/description/

from collections import defaultdict, deque
from typing import List, DefaultDict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the adjacency list and in-degree array
        graph: dict[int, List[int]] = defaultdict(list)
        in_degree: List[int] = [0] * numCourses

        #----------------------------------------
        for course, requirement in prerequisites:
            graph[requirement].append(course)
            in_degree[course] += 1
        #----------------------------------------

        # Initialize queue with all courses having zero in-degree (no prerequisites)
        queue: deque[int] = deque([i for i in range(numCourses) if in_degree[i] == 0])
        visited: int = 0  # Count of courses that can be taken

        #----------------------------------------
        while queue:
            course: int = queue.popleft()
            visited += 1
            #----------------------------------------
            for neighbor in graph[course]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
            #----------------------------------------
        #----------------------------------------

        # If all courses have been visited, it's possible to finish all
        return visited == numCourses
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


p = [[1, 0], [2, 1], [2, 5], [0, 3], [4, 3], [3, 5], [4, 5]]
sol = Solution()

print(sol.canFinish(6, p))