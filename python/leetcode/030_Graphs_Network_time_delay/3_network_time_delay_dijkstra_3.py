# https://leetcode.com/problems/network-delay-time/description/

import heapq
from collections import defaultdict


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list : defaultdict[int, list[tuple[int,int]]] = defaultdict(list)
        
        #----------------------------------------
        for from_node, to_node, time_needed in times:
            adj_list[from_node].append((to_node, time_needed))
        #----------------------------------------
        
        heap : list[ tuple[int,int] ] = [(0,k)]
        
        shortest_time : dict[int,int] = {}
        
        #----------------------------------------
        while heap:
            current_time, current_vertex = heapq.heappop(heap)
            
            if current_vertex in shortest_time: continue
            
            shortest_time[current_vertex] = current_time
            
            #----------------------------------------
            for neigh_vertex, neigh_time in adj_list[current_vertex]:
                if neigh_vertex not in shortest_time:
                    new_time = current_time + neigh_time
                    heapq.heappush(heap, (new_time, neigh_vertex))
            #----------------------------------------
        #----------------------------------------
        
        max_time = max(shortest_time.values())
        return max_time if len(shortest_time) == n else -1
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