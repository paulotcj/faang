# https://leetcode.com/problems/network-delay-time/description/
import heapq


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime_1(self, times: list[list[int]], n: int, k: int) -> int:
        distances = [float('inf')] * n
        
        distances[k - 1] = 0
        #----------------------------------------
        for i in range(n - 1):
            count = 0
            #----------------------------------------
            for j in range(len(times)):
                source = times[j][0]
                target = times[j][1]
                weight = times[j][2]
                
                if distances[source - 1] + weight < distances[target - 1]:
                    distances[target - 1] = distances[source - 1] + weight
                    count += 1
            #----------------------------------------
            
            if count == 0:
                break
        #----------------------------------------
        
        ans = max(distances)
        return -1 if ans == float('inf') else ans
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