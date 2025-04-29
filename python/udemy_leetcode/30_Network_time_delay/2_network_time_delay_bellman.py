
# https://leetcode.com/problems/network-delay-time/description/
import heapq
from math import inf

from typing import List


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime_old(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [float('inf')] * n
        
        distances[k - 1] = 0
        for i in range(n - 1):
            count = 0
            for j in range(len(times)):
                source = times[j][0]
                target = times[j][1]
                weight = times[j][2]
                
                if distances[source - 1] + weight < distances[target - 1]:
                    distances[target - 1] = distances[source - 1] + weight
                    count += 1
            
            if count == 0:
                break
        
        ans = max(distances)
        return -1 if ans == float('inf') else ans
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialize distances with "infinity" except for the starting node k
        dist = [float('inf')] * (n + 1) # n+1 because if we had a n = 3 we would have [inf, inf, inf], and we want to simply not have to deal with issues at index zero, so we want [inf, inf, inf, inf]
        dist[k] = 0 # start node gets distance 0

        # Relax all edges up to n-1 times
        for _ in range(n - 1):
            for u, v, w in times:
                if dist[u] != float('inf') and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    
        # Bellman-Ford sets impossible paths to inf, so we check if any node was never updated
        answer = max(dist[1:])  # ignore index 0
        return -1 if answer == float('inf') else answer

        """
        Explanation:
        - Bellman-Ford systematically relaxes all edges in the graph up to n-1 times.
        - Each relaxation tries to improve the best known distance to each node.
        - If after n-1 iterations a node's distance remains infinity, it means it's unreachable.
        """
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



sol = Solution()
t = [[1, 4, 2], [1, 2, 9], [4, 2, -4], [2, 5, -3], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(sol.networkDelayTime(t, 5, 1))