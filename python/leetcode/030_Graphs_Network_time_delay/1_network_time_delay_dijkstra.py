# https://leetcode.com/problems/network-delay-time/description/


import heapq
from math import inf

#-------------------------------------------------------------------------
class Solution:
    # n - from 1 to 10 (the number of nodes in the system)
    # times - an array containing a list of list, the internal list is of size 3, the first number is 
    #   the source node, the second the destination node, and the third is the time cost to traverse
    # k - source signal node
    # now return the time necessary to inform all nodes. If not possible to inform all nodes return -1
    #   that means we have to traverse to all nodes, and find the shortest path to that node, and also
    #   keep track if we visited all nodes, otherwise the answer should be -1
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        time_req_list : list[int] = [inf] * n # all vertices are set to inf time, if we don't reach any of these nodes then we will know
        adj_list : list[list[int]] = [ [] for _ in range(n) ]
        
        time_req_list[k - 1] = 0 # set root vertex time to reach itself to zero
        
        #----------------------------------------
        for from_vertex, to_vertex, time_needed in times:
            adj_list[from_vertex - 1].append( ( to_vertex - 1, time_needed ) ) # from_vertex -1 -> remember we need to offset the idx
        #----------------------------------------

        heap : list[tuple[int,int]] = [(0, k - 1)]
        #----------------------------------------
        while heap:
            current_time, current_vertex = heapq.heappop(heap)
            
            # note that all values at time_req_list start with inf, so we will look at every node at least once
            if current_time > time_req_list[current_vertex]: continue # we alread have a lower time, then skip this - but should we check its children?
            
            # then current time must be less or equal to time_req_list[current_vertex]
            time_req_list[current_vertex] = current_time
            
            #----------------------------------------
            for neigh_vertex, neigh_time_needed in adj_list[current_vertex]:
                
                new_time : int = neigh_time_needed + current_time
                
                #----------------------------------------
                if new_time < time_req_list[neigh_vertex]: #found a new shorter path
                    time_req_list[neigh_vertex] = new_time
                    
                    heapq.heappush(heap, (new_time, neigh_vertex))
                #----------------------------------------
            #----------------------------------------
        #----------------------------------------
        
        #return the answer
        max_time : int = max(time_req_list)
        
        return -1 if max_time == inf else max_time
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


