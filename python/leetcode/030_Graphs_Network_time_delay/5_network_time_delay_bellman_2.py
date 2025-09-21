# https://leetcode.com/problems/network-delay-time/description/
import heapq


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime_2(self, times: list[list[int]], n: int, k: int) -> int:
        # Initialize distances with "infinity" except for the starting node k
        dist : list[int] = [float('inf')] * (n + 1) # n+1 because if we had a n = 3 we would have [inf, inf, inf], and we want to simply not have to deal with issues at index zero, so we want [inf, inf, inf, inf]
        dist[k] = 0 # start node gets distance 0

        #----------------------------------------
        
        for _ in range(n - 1): # the n-1 is given from bellman-ford algorithm
            
            #----------------------------------------
            for from_node, to_node, time_needed in times:
                
                ''' note: distance here is used as time-distance
                The logic below is, if the distance to the current node is known, then we can
                compute or compare the added distence to the neighbour (target) node. Otherwise we 
                would be calculating inf + some_number which would be inf anyway.
                After that then we need to compare if: the distance of the from_node plus the edge's
                distance is smaller than the current distance of the to_node's distance. If yes, then a 
                new shortest path was found, and we update the distance.'''
                if dist[from_node] != float('inf'): # if the distance to this node is known
                    
                    # if the distance from 'from_node' plus time needed is smaller than the currently 
                    #  known distance to 'to_node' then update 'to_node' distance
                    if ( dist[from_node] + time_needed ) < dist[to_node]: 
                        dist[to_node] = dist[from_node] + time_needed
            #----------------------------------------
        #----------------------------------------
                    
        # Bellman-Ford sets impossible paths to inf, so we check if any node was never updated
        max_distance : int = max(dist[1:])  # ignore index 0
        return -1 if max_distance == float('inf') else max_distance

        """
        Explanation:
        - Bellman-Ford systematically relaxes all edges in the graph up to n-1 times.
        - Each relaxation tries to improve the best known distance to each node.
        - If after n-1 iterations a node's distance remains infinity, it means it's unreachable.
        """
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