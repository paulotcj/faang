
# https://leetcode.com/problems/network-delay-time/description/
import heapq
from math import inf

from typing import List


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
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



sol = Solution()
t = [[1, 4, 2], [1, 2, 9], [4, 2, -4], [2, 5, -3], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(sol.networkDelayTime(t, 5, 1))