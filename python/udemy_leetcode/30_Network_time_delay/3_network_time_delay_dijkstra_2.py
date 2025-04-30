# https://leetcode.com/problems/network-delay-time/description/

# from heapq import heappop, heappush

import heapq
from collections import defaultdict
from typing import List, Tuple, Dict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        pass
    #-------------------------------------------------------------------------
    def networkDelayTime_old(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the graph as an adjacency list
        graph : defaultdict[ int, List[ Tuple[int,int] ] ] = defaultdict(list) # any key not present, the default value is a list
        for from_node, to_node, time_needed in times:
            graph[from_node].append((to_node, time_needed))
        
        # Min-heap to store (time, node)
        heap : List[ Tuple[int,int] ] = [(0, k)] # put in the first element, root vertex with distance of zero
        
        # Dictionary to store the shortest time to reach each node
        shortest_time : Dict[int, int] = {}
        
        #-----------------------------------
        while heap:
            current_time, current_vertex = heapq.heappop(heap)
            
            # If the node is already visited, skip it
            if current_vertex in shortest_time:
                continue
            
            # Record the shortest time to reach this node
            shortest_time[current_vertex] = current_time
            
            #-----------------------------------
            # Explore neighbors
            for neigh_vertex, neigh_time_needed in graph[current_vertex]:
                
                if neigh_vertex not in shortest_time:
                    new_time = current_time + neigh_time_needed
                    heapq.heappush(heap, (new_time, neigh_vertex))
            #-----------------------------------
        #-----------------------------------
        
        # If all nodes are reached, return the maximum time; otherwise, return -1
        return max(shortest_time.values()) if len(shortest_time) == n else -1
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
