# https://leetcode.com/problems/network-delay-time/description/
import heapq


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        dist: list[int] = [float('inf')] * (n+1)
        dist[k] = 0
        
        #----------------------------------------
        # Relax all edges up to n-1 times
        for _ in range(n-1): # the n-1 is given from bellman-ford algorithm
            
            # An optimization, since we don't need to loop until n-1 if we havent found
            #  a new shortest path in the loop, meaning, no shorther path will be found
            #  in any future loops
            new_shortest_path_found = False
            #----------------------------------------
            for from_node, to_node, time_needed in times:
                if dist[from_node] != float('inf'): #this node has a known distance so we can calculate the steps below
                    dist_from_node_plus_time_needed = dist[from_node] + time_needed
                    if dist_from_node_plus_time_needed < dist[to_node]: # we found a shorter path to 'to_node'
                        dist[to_node] = dist_from_node_plus_time_needed
                        new_shortest_path_found = True
            #----------------------------------------
            if new_shortest_path_found is False:
                break
        #----------------------------------------
        
        max_distance : int = max(dist[1:]) #slice from idx 1 to the end in order to ignore idx 0
        return max_distance if max_distance != float('inf') else -1
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