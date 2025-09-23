# https://leetcode.com/problems/network-delay-time/description/

import heapq
from collections import defaultdict

#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        adj_list : defaultdict[int, list[int]] = defaultdict(list)
        priority_queue : list[list[int]] = [ [0, k] ] # Min-heap to store [time , node] - it needs to be in this order unfortunately
        shortest_time : dict[int, int] = {}        

        #----------------------------------------
        for from_node, to_node, time_required in times :
            adj_list[from_node].append( [to_node, time_required] )
        #----------------------------------------

        #----------------------------------------
        while priority_queue :
            curr_node_time , curr_node = heapq.heappop(priority_queue)

            if curr_node in shortest_time : continue

            shortest_time[curr_node] = curr_node_time

            #----------------------------------------
            for to_node , to_node_time in adj_list[curr_node] :
                if to_node in shortest_time : continue
                new_time : int = to_node_time + curr_node_time
                heapq.heappush(priority_queue, [ new_time , to_node ] )
            #----------------------------------------
        #----------------------------------------

        max_time : int = max(shortest_time.values())

        result : int = max_time if len(shortest_time) == n else -1

        return result
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