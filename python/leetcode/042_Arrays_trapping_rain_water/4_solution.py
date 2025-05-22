# https://leetcode.com/problems/trapping-rain-water/
from typing import List

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def trap(self, height: List[int]) -> int:
        len_hei: int = len(height)
        
        if len_hei == 0: return 0

        left_idx  : int = 0
        right_idx : int = len_hei - 1
        left_max_v  : int = 0
        right_max_v : int = 0
        total_trapped_water : int = 0

        #-----------------------------------
        while left_idx < right_idx:
            left_v : int = height[left_idx]
            right_v : int = height[right_idx]
            
            #----------
            if left_v < right_v:
                if left_v >= left_max_v:
                    left_max_v : int = left_v
                else:
                    total_trapped_water += left_max_v - left_v
                left_idx += 1
            else:
                if right_v >= right_max_v:
                    right_max_v : int = right_v
                else:
                    total_trapped_water += right_max_v - right_v
                right_idx -= 1
            #----------
        #-----------------------------------

        return total_trapped_water
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def trap2(self, height: List[int]) -> int:
        len_hei: int = len(height)
        
        if len_hei == 0: return 0

        left_idx  : int = 0
        right_idx : int = len_hei - 1
        left_max_v  : int = 0
        right_max_v : int = 0
        total_trapped_water : int = 0

        #-----------------------------------
        while left_idx < right_idx:
            if height[left_idx] < height[right_idx]:
                if height[left_idx] >= left_max_v:
                    left_max_v : int = height[left_idx]
                else:
                    total_trapped_water += left_max_v - height[left_idx]
                left_idx += 1
            else:
                if height[right_idx] >= right_max_v:
                    right_max_v : int = height[right_idx]
                else:
                    total_trapped_water += right_max_v - height[right_idx]
                right_idx -= 1
        #-----------------------------------

        return total_trapped_water
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


sol = Solution()
input = [0,1,2,1]
expected = 0
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')
# exit(0)
    
sol = Solution()
input = [0,1,0,2,1,0,1,3,2,1,2,1]
expected = 6
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [4,2,0,3,2,5]
expected = 9
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')

sol = Solution()
input = [5,5,1,7,1,1,5,2,7,6]
expected = 23
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')



sol = Solution()
input = [9,2,1,1,6,4,0,4,4]
expected = 18
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')


sol = Solution()
input = [9,2,1,1,6,4,0,4,4,0,0,0]
expected = 18
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')


sol = Solution()
input = [0,0,0]
expected = 0
result = sol.trap(input)
# print(input)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('------------------')
