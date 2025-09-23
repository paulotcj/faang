# https://leetcode.com/problems/network-delay-time/description/


#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        time : list[int] = [float('inf')] * (n + 1) # n+1 because if we had a n = 3 we would have [inf, inf, inf], and we want to simply not have to deal with issues at index zero, so we want [inf, inf, inf, inf]
        time[k] = 0

        # Relax all edges up to n-1 times
        #----------------------------------------
        for _ in range(n-1) : # the n-1 is given from bellman-ford algorithm

            # An optimization, since we don't need to loop until n-1 if we havent found
            #  a new shortest path in the loop, meaning, no shorther path will be found
            #  in any future loops
            new_shortest_path_found : bool = False

            #----------------------------------------
            for from_node, to_node, time_needed in times:
                if time_needed == float('inf') : continue # this node doesnt have a known time, we cant calculate anything from here
                from_node_new_time : int = time[from_node] + time_needed
                if from_node_new_time < time[to_node] :
                    time[to_node] = from_node_new_time
                    new_shortest_path_found = True
            #----------------------------------------
            if new_shortest_path_found == False : break
        #----------------------------------------

        max_time : int = max( time[1:] ) #slice from idx 1 to the end in order to ignore idx 0
        return max_time if max_time != float('inf') else -1
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