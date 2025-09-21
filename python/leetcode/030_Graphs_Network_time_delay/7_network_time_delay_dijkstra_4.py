# https://leetcode.com/problems/network-delay-time/description/
import heapq

from typing import List, Dict
import heapq  # For priority queue implementation
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Step 1: Build the adjacency list representation of the graph
        graph: Dict[int, List[tuple[int, int]]] = {i: [] for i in range(1, n + 1)}

        #----------------------------------------
        for u, v, w in times:
            graph[u].append((v, w))  # Append (target node, weight)
        #----------------------------------------

        # Step 2: Use a priority queue to implement Dijkstra's algorithm
        min_heap: List[tuple[int, int]] = [(0, k)]  # (time, node)
        shortest_time: Dict[int, int] = {}  # To store the shortest time to each node

        #----------------------------------------
        while min_heap:
            current_time, current_node = heapq.heappop(min_heap)

            # If the node is already visited, skip it
            if current_node in shortest_time:
                continue

            # Record the shortest time to reach this node
            shortest_time[current_node] = current_time

            #----------------------------------------
            # Explore neighbors
            for neighbor, travel_time in graph[current_node]:
                if neighbor not in shortest_time:
                    heapq.heappush(min_heap, (current_time + travel_time, neighbor))
            #----------------------------------------
        #----------------------------------------

        # Step 3: Check if all nodes are reachable
        if len(shortest_time) != n:
            return -1

        # Step 4: Return the maximum time among all shortest paths
        return max(shortest_time.values())
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------    




sol = Solution()
# Test case
# times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes
#  in other words: [1, 2, 9] -> from node 1 to node 2 takes 9 units of time
#  [1, 4, 2] -> from node 1 to node 4 takes 2 units of time
times : list[list[int]] = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
n : int = 5
k : int = 1
expected : int = 14
result : int = sol.networkDelayTime(times = times, n = n, k = k)
print(f'result : {result} - expected : {expected} - is the result correct : {result == expected}')
print('-------------')


times = [[2,1,1],[2,3,1],[3,4,1]] 
n = 4
k = 2
expected : int = 2
result : int = sol.networkDelayTime(times = times, n = n, k = k)
print(f'result : {result} - expected : {expected} - is the result correct : {result == expected}')
print('-------------')


times = [[1,2,1]]
n = 2
k = 1
expected : int = 1
result : int = sol.networkDelayTime(times = times, n = n, k = k)
print(f'result : {result} - expected : {expected} - is the result correct : {result == expected}')
print('-------------')


times = [[1,2,1]]
n = 2
k = 2
expected : int = -1
result : int = sol.networkDelayTime(times = times, n = n, k = k)
print(f'result : {result} - expected : {expected} - is the result correct : {result == expected}')
print('-------------')