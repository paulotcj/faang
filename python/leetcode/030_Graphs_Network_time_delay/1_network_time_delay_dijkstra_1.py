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
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int :
        time_req_list : list[int] = [inf] * n # all vertices are set to inf time, if we don't reach any of these nodes then we will know
        adj_list : list[list[int]] = [ [] for _ in range(n) ]

        time_req_list[k - 1] = 0 # set root vertex time to reach itself to zero, and K-1 because K is not base zero
        #----------------------------------------
        for from_vertex, to_vertex, time_needed in times :
            adj_list[ from_vertex-1 ].append( [to_vertex-1 , time_needed] ) # from_vertex -1 -> remember we need to offset the idx
        #----------------------------------------

        priority_queue : list[list[int]] = [ [ k - 1 , 0 ] ] # vertex , time to reach it
        #----------------------------------------
        while priority_queue :
            curr_vertex , curr_time_needed = heapq.heappop( priority_queue )

            # note that all values at time_req_list start with inf, so we will look at every node at least once
            ''' added explanation because this condition is tricky: if curr_time_needed == time_req_list[curr_vertex] then the node should still 
              be processed to explore its neighbors, as there might be other paths that depend on this node. Additionally, if the condition were >=, 
              the algorithm would skip processing nodes even when curr_time_needed == time_req_list[curr_vertex] - this could lead to missing 
              valid paths to other nodes that depend on this node being processed. by using '>' the algorithm ensures that only strictly worse 
              paths are ignored. This maintains the correctness of Dijkstra's algorithm, as it guarantees that all shortest paths are explored
            '''
            if curr_time_needed > time_req_list[curr_vertex] : continue

            # then current time must be less or equal to time_req_list[current_vertex]
            time_req_list[curr_vertex] = curr_time_needed

            #----------------------------------------
            for to_vertex , to_vertex_time in adj_list[curr_vertex] :
                new_time : int = to_vertex_time + curr_time_needed

                #-----
                if new_time < time_req_list[to_vertex] : #found a new shorter path
                    time_req_list[to_vertex] = new_time
                    heapq.heappush( priority_queue , [to_vertex, new_time] )
                #-----
            #----------------------------------------
        #----------------------------------------

        max_time : int = max(time_req_list)
        result : int = max_time if max_time != inf else -1
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


