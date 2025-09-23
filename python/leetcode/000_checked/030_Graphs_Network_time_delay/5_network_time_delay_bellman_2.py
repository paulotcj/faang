# https://leetcode.com/problems/network-delay-time/description/


#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # Initialize times with "infinity" except for the starting node k
        time_needed_list : list[int] = [ float('inf') ] * (n+1) # n+1 because if we had a n = 3 we would have [inf, inf, inf], and we want to simply not have to deal with issues at index zero, so we want [inf, inf, inf, inf]
        time_needed_list[k] = 0

        #----------------------------------------
        for _ in range(n - 1) : # the n-1 is given from bellman-ford algorithm
            #----------------------------------------
            for from_node, to_node, time_needed in times :

                ''' the logic below is, if the time to the from_node is known, then we can
                compute or compare the added time to to_node. Otherwise we would be calculating 
                inf + some_number which would be infinity anyway.
                After that then we need to compare if: the distance of the from_node plus the edge's
                distance is smaller than the current distance of the to_node's distance. If yes, then a 
                new shortest path was found, and we update the distance.'''
                if time_needed_list[from_node] == float('inf') : continue # the time to this node is not know, there's nothing we can do now

                # if the time from 'from_node' plus time needed is smaller than the currently 
                #  known time to 'to_node' then update 'to_node' time
                from_node_new_time : int = time_needed_list[from_node] + time_needed
                if from_node_new_time < time_needed_list[to_node] : 
                    time_needed_list[to_node] = from_node_new_time
            #----------------------------------------
        #----------------------------------------

        max_time : int = max(time_needed_list[1:]) # slice the array, we can't use index 0 as it will always be float('inf')

        result : int = max_time if max_time != float('inf') else -1

        return result
    
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