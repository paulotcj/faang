# https://leetcode.com/problems/trapping-rain-water/
from typing import List, Tuple
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def _find_first_left(self) -> Tuple[int,int]: # find the first occurence of a non zero height
        for idx, val in enumerate(self.height):
            if val > 0 : return (idx,val)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _find_first_right(self) -> Tuple[int,int]:
        for idx, val in enumerate(self.height[::-1]): # loop backwards
            if val > 0: #found the first non zero, so... a wall
                idx_aux : int = (len(self.height) - 1) - idx # is this how many steps from the last idx?
                ret_val : Tuple[int,int] = (idx_aux, val)
                return ret_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def _update_max_and_get_values(self, left_i : int, right_i : int) -> Tuple[int,int]:
        ''' get the values for left_i and right_i, and try to update the max
        values for self.max_left and self.max_right'''
        left_v : int = self.height[left_i]
        right_v : int = self.height[right_i]
        
        self.max_left : int = max(self.max_left, left_v)    # i don't get it why we use those
        self.max_right : int = max(self.max_right, right_v)
        
        return (left_v, right_v)
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
        if len(height) < 3 : return 0 # you need at least a wall, a well, and a wall
        
        self.height : List[int] = height
        self.total_water : int = 0
        
        left_i , self.max_left = self._find_first_left() # find the first occurence of a non zero height
        right_i, self.max_right = self._find_first_right() # number of backwards steps from the non-zero value, and the height value
        var_bs = 0
        #-----------------------------------
        while left_i < right_i:
            # get the values for left and right, but at the same time update max_left and
            #   max_right if a new max value is found
            left_v , right_v = self._update_max_and_get_values(left_i = left_i, right_i = right_i)
            
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

