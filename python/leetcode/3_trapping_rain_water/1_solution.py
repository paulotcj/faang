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

