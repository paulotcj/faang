#problem: https://leetcode.com/problems/trapping-rain-water/
from typing import List
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def __find_max_left(self, height: List[int], index: int) -> int:
        if index <= 0 or index >= len(height): return 0
        return max(height[:index])
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __find_max_right(self, height: List[int], index: int) -> int:
        index += 1
        if index < 0 or index >= len(height): return 0
        return max(height[index:])
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def trap3(self, height: List[int]) -> int:
        total_water = 0

        for i, v in enumerate(height):
            max_left = self.__find_max_left(height, i)
            max_right = self.__find_max_right(height, i)

            current_water = min(max_left, max_right) - v

            if current_water > 0:
                total_water += current_water

        return total_water
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __find_first_left(self, height: List[int]) -> List[int]:
        for i , v in enumerate(height):
            if v > 0:
                return i, v
    #-------------------------------------------------------------------------
    def __find_first_right(self, height: List[int]) -> List[int]:
        for i, v in enumerate(height[::-1]):
            if v > 0:
                return (len(height) - 1) - i , v
    #-------------------------------------------------------------------------
    def __handle_values(self,height: List[int], left_i: int, right_i: int) -> List[int]:
            left_v = height[left_i]
            right_v = height[right_i]
            self.max_left = max(self.max_left, left_v)
            self.max_right = max(self.max_right, right_v)
            return left_v , right_v
    #-------------------------------------------------------------------------
    def __handle_left(self, left_v: int) -> None:
        if left_v < self.max_left:
            current_water = min(self.max_left, self.max_right) - left_v
            self.total_water += current_water
    #-------------------------------------------------------------------------        
    def __handle_right(self, right_v: int) -> None:
        if right_v < self.max_right:
            current_water = min(self.max_left, self.max_right) - right_v
            self.total_water += current_water
    #-------------------------------------------------------------------------
    def trap2(self, height: list[int]) -> int:
        if len(height) <= 2: return 0
        self.total_water: int = 0
        left_i, self.max_left = self.__find_first_left(height)
        right_i , self.max_right = self.__find_first_right(height)
        while left_i < right_i:
            left_v , right_v = self.__handle_values(height, left_i, right_i)
            #---
            if left_v <= right_v:
                self.__handle_left(left_v = left_v)
                left_i += 1
            else:
                self.__handle_right(right_v = right_v)
                right_i -= 1
            #---
        #---
        return self.total_water
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def trap(self, height: List[int]) -> int:
        left_i, right_i = 0, len(height) -1

        total_water = 0
        maxLeft = height[left_i]
        maxRight = height[right_i]

        while left_i < right_i:
            #---
            if maxLeft < maxRight:
                left_i += 1
                maxLeft = max(maxLeft, height[left_i])
                total_water += maxLeft - height[left_i]
            else:
                right_i -= 1
                maxRight = max(maxRight, height[right_i])
                total_water += maxRight - height[right_i]
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
exit(0)
    
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

