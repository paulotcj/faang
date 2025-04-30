# https://leetcode.com/problems/network-delay-time/description/

# from heapq import heappop, heappush

import heapq
from collections import defaultdict
from typing import List, Tuple, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    
    #-------------------------------------------------------------------------
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        pass
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the graph as an adjacency list
        adj_list : defaultdict[ int, List[ Tuple[int,int] ] ] = defaultdict(list) # any key not present, the default value is a list
        for from_node, to_node, time_needed in times:
            adj_list[from_node].append((to_node, time_needed))
        
        # Min-heap to store (time, node)
        heap : List[ Tuple[int,int] ] = [(0, k)] # put in the first element, root vertex with distance of zero
        
        # Dictionary to store the shortest time to reach each node
        shortest_time : Dict[int, int] = {}
        
        #-----------------------------------
        ''' In this min-heap-based Dijkstra approach, the first time a node is popped 
        from the heap, we have already found its shortest distance (because the heap 
        ensures we always pop the smallest current distance). Therefore, once a node 
        is in the shortest_time dictionary, no shorter path can appear afterward, so 
        it's safe to skip that node.
        '''
        while heap:
            current_time, current_vertex = heapq.heappop(heap)
            
            # If the node is already visited, skip it
            if current_vertex in shortest_time:
                continue
            
            # Record the shortest time to reach this node
            shortest_time[current_vertex] = current_time
            
            #-----------------------------------
            # Explore neighbors
            for neigh_vertex, neigh_time_needed in adj_list[current_vertex]:
                
                if neigh_vertex not in shortest_time:
                    new_time = current_time + neigh_time_needed
                    heapq.heappush(heap, (new_time, neigh_vertex))
            #-----------------------------------
        #-----------------------------------
        
        # If all nodes are reached, return the maximum time; otherwise, return -1
        return max(shortest_time.values()) if len(shortest_time) == n else -1
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


sol = Solution()
# Test case
# times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes
#  in other words: [1, 2, 9] -> from node 1 to node 2 takes 9 units of time
#  [1, 4, 2] -> from node 1 to node 4 takes 2 units of time
t = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(sol.networkDelayTime(t, 5, 1))