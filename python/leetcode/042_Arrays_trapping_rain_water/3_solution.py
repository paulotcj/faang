# https://leetcode.com/problems/trapping-rain-water/
from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def trap(self, height: List[int]) -> int:
        left_i, right_i = 0, len(height) -1

        total_water = 0
        max_left = height[left_i] #We can start from the edges and consider them max values
        max_right = height[right_i]

        while left_i < right_i:
            #---
            # we only move inwards based on the walls max values, since inwards walls might be bigger
            # so we are always looking for them, but as we scan, if there's a wall we calculate the potential
            #  water from that spot
            if max_left <= max_right: 
                left_i += 1 #note: we can do this from the start, because either the first index does form a wall and therefore we don't need to worry, or does not and again, we don't need to worry
                max_left = max(max_left, height[left_i]) #the current value ay or may not be the new wall
                curr_water = max_left - height[left_i] #now if Max_Left is bigger than our current value, that means water would be trapped
                total_water += curr_water
            else:
                right_i -= 1
                max_right = max(max_right, height[right_i])
                curr_water = max_right - height[right_i]
                total_water += curr_water
            #---
        #---
              
        return total_water    
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


sol = Solution()
input = [0,1,2,1]
expected = 0
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')
# exit(0)
    
sol = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
expected = 6
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [4,2,0,3,2,5]
expected = 9
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [5,5,1,7,1,1,5,2,7,6]
expected = 23
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [9,2,1,1,6,4,0,4,4]
expected = 18
result = sol.trap(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

