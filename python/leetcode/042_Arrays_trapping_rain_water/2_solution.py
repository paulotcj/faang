# https://leetcode.com/problems/trapping-rain-water/
from typing import List, Tuple
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def _find_first_left(self) -> Tuple[int,int]:
        for i , v in enumerate(self.height):
            if v > 0:
                return (i, v)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _find_first_right(self) -> Tuple[int,int]:
        for i, v in enumerate(self.height[::-1]):
            if v > 0:
                return ((len(self.height) - 1) - i , v)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _handle_values(self, left_i: int, right_i: int) -> Tuple[int,int]:
            left_v = self.height[left_i]
            right_v = self.height[right_i]
            self.max_left = max(self.max_left, left_v)
            self.max_right = max(self.max_right, right_v)
            return (left_v , right_v)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _handle_left(self, left_v: int) -> None:
        if left_v < self.max_left:
            current_water = min(self.max_left, self.max_right) - left_v
            self.total_water += current_water
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------     
    def _handle_right(self, right_v: int) -> None:
        if right_v < self.max_right:
            current_water = min(self.max_left, self.max_right) - right_v
            self.total_water += current_water
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    # def trap(self, height: list[int]) -> int:
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def trap(self, height: list[int]) -> int:
        if len(height) <= 2: return 0
        
        self.height : List[int] = height
        self.total_water: int = 0
        left_i, self.max_left = self._find_first_left()
        right_i , self.max_right = self._find_first_right()
        
        #-----------------------------------
        while left_i < right_i:
            left_v , right_v = self._handle_values(left_i, right_i)
            
            if left_v <= right_v:
                self._handle_left(left_v = left_v)
                left_i += 1
            else:
                self._handle_right(right_v = right_v)
                right_i -= 1
        #-----------------------------------
        
        return self.total_water
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

