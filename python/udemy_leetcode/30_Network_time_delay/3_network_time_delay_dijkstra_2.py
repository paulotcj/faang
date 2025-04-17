from heapq import heappop, heappush
from collections import defaultdict
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Build the graph as an adjacency list
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
        
        # Min-heap to store (time, node)
        heap = [(0, k)]
        # Dictionary to store the shortest time to reach each node
        shortest_time = {}
        
        while heap:
            time, node = heappop(heap)
            
            # If the node is already visited, skip it
            if node in shortest_time:
                continue
            
            # Record the shortest time to reach this node
            shortest_time[node] = time
            
            # Explore neighbors
            for neighbor, weight in graph[node]:
                if neighbor not in shortest_time:
                    heappush(heap, (time + weight, neighbor))
        
        # If all nodes are reached, return the maximum time; otherwise, return -1
        return max(shortest_time.values()) if len(shortest_time) == n else -1
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
