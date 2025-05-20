# https://leetcode.com/problems/trapping-rain-water/
from typing import List, Tuple
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def _find_first_left(self) -> Tuple[int,int]: # find the first occurence of a non zero height
        for idx, val in enumerate(self.height):
            if val > 0 : 
                ret_val : Tuple[int,int] = (idx,val)
                return ret_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _find_first_right(self) -> Tuple[int,int]: # find the first occurence of a non zero height from the right side 
        
        # you need eto convert the output of enumerate to a list as enumerate is not reversible
        #  so the logic is, get the idx and val from self.height via enumerate. convert it
        #  to a list as it's necessary, then reverse it.
        for idx, val in reversed(list(enumerate(self.height))):
            if val > 0:
                ret_val : Tuple[int,int] = (idx, val)
                return ret_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _calculate_water_level(self, terrain_height : int, left_side : bool = False, 
      right_side : bool = False) -> None:
        
        if (left_side == True and terrain_height < self.max_left ) or \
          (right_side == True and terrain_height < self.max_right ):
              
            potential_water_level : int = min(self.max_left, self.max_right)
            current_water_level : int = potential_water_level - terrain_height
            self.total_water += current_water_level
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def trap(self, height: list[int]) -> int:
        #---------------------
        # basic house keeping and setting up vars
        if len(height) < 3 : return 0 # you need at least a wall, a well, and a wall
        self.height : List[int] = height
        self.total_water : int = 0
        #---------------------
        # we are just looking to find the first non zero value of the left and right walls , and that's it
        left_i , self.max_left = self._find_first_left() # find the first occurence of a non zero height from the left side
        right_i, self.max_right = self._find_first_right() # find the first occurence of a non zero height from the right side
        #---------------------
        
        #-----------------------------------
        while left_i < right_i:
            left_v  : int = self.height[left_i]
            right_v : int = self.height[right_i]
            
            self.max_left  : int = max(self.max_left, left_v)
            self.max_right : int = max(self.max_right, right_v)            
            
            if left_v <= right_v:
                # self._process_left_bar(left_v = left_v)
                self._calculate_water_level(terrain_height=left_v, left_side=True)
                left_i += 1
            else:
                # self._process_right_bar(right_v = right_v)
                self._calculate_water_level(terrain_height=right_v, right_side=True)
                right_i -= 1
        #-----------------------------------
        return self.total_water
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
