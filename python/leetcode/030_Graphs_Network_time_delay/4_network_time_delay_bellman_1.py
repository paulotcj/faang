# https://leetcode.com/problems/network-delay-time/description/


''' Note 1: this implementation does not check for negative cycles, as Bellman-Ford loops
  for n-1, as it would then guarantee the shortest path, but if we wanted to check for
  negative cycles we would run this one last time, and if after n-1 we could still find
  a new shortest path, that means we are in a negative cycle.
Note 2 : Another question about Bellman-Ford is why we loop 'n-1' times. The reason is 
  that at the worst possible case, any graph is connected by n-1 edges/lind. If we find more 
  than n-1 edges/links that means we are in a cycle, for instance:
  Nodes: A , B , C , D   Connections: A -> B -> C -> D  We can observe 3 edges/links

Note 3 : IMPORTANT - Checking for negative cycles implemented
'''
#-------------------------------------------------------------------------
class Solution :
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        # because we ase using a distance list and not a default dict, we need to convert the basing index to -1
        time_req_list : list[int] = [ float('inf') ] * n
        time_req_list[k-1] = 0

        #----------------------------------------
        for _ in range( n - 1 ) : # bellman-ford approach, always loop for n-1 edges/links
            new_time_found_flag : bool = False
            #----------------------------------------
            for from_node, to_node, time_req in times :

                from_node_new_time : int = time_req_list[from_node - 1] + time_req

                #-----
                if from_node_new_time < time_req_list[to_node - 1] :
                    time_req_list[to_node - 1] = from_node_new_time
                    new_time_found_flag = True
                #-----
            #----------------------------------------
            if new_time_found_flag == 0 : break
        #----------------------------------------

        # additional iteration to check for negative weight cycles - simple solution
        #----------------------------------------
        for from_node, to_node, time_req in times :
            from_node_new_time : int = time_req_list[from_node - 1] + time_req
            if from_node_new_time < time_req_list[to_node - 1] :
                return - 1 # negative weight cycle detected
        #----------------------------------------  

        max_time : int = max(time_req_list)
        result : int = max_time if max_time != float('inf') else -1
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