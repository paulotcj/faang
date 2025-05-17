
# https://leetcode.com/problems/network-delay-time/description/
import heapq


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
        dist: List[int] = [float('inf')] * (n+1)
        dist[k] = 0
        
        #-----------------------------------
        # Relax all edges up to n-1 times
        for _ in range(n-1): # the n-1 is given from bellman-ford algorithm
            
            # An optimization, since we don't need to loop until n-1 if we havent found
            #  a new shortest path in the loop, meaning, no shorther path will be found
            #  in any future loops
            new_shortest_path_found = False
            #-----------------------------------
            for from_node, to_node, time_needed in times:
                if dist[from_node] != float('inf'): #this node has a known distance so we can calculate the steps below
                    dist_from_node_plus_time_needed = dist[from_node] + time_needed
                    if dist_from_node_plus_time_needed < dist[to_node]: # we found a shorter path to 'to_node'
                        dist[to_node] = dist_from_node_plus_time_needed
                        new_shortest_path_found = True
            #-----------------------------------
            if new_shortest_path_found is False:
                break
        #-----------------------------------
        
        max_distance : int = max(dist[1:]) #slice from idx 1 to the end in order to ignore idx 0
        return max_distance if max_distance != float('inf') else -1
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def networkDelayTime2(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialize distances with "infinity" except for the starting node k
        dist : List[int] = [float('inf')] * (n + 1) # n+1 because if we had a n = 3 we would have [inf, inf, inf], and we want to simply not have to deal with issues at index zero, so we want [inf, inf, inf, inf]
        dist[k] = 0 # start node gets distance 0

        #-----------------------------------
        
        for _ in range(n - 1): # the n-1 is given from bellman-ford algorithm
            
            #-----------------------------------
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
            #-----------------------------------
        #-----------------------------------
                    
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

# times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes
#  in other words: [1, 2, 9] -> from node 1 to node 2 takes 9 units of time
#  [1, 4, 2] -> from node 1 to node 4 takes 2 units of time
t = [[1, 4, 2], [1, 2, 9], [4, 2, -4], [2, 5, -3], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(sol.networkDelayTime(t, 5, 1))