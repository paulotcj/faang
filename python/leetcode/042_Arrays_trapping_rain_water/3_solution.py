# https://leetcode.com/problems/trapping-rain-water/
from typing import List

''' start with house keeping, set 'total_water' to zero, seet the left_index to 0 set the right_index
to len(height) - 1 (e.g.: 10 - 1 = 9 which is the idx of the last element in the array). And from there
we set the 'v_max_left' and 'v_max_right' according to their indexes. The difference here from the
previous approach is that we realized we don't need to care for the values of left or right, the
algorithm will sort it out if the extremeties have values of 0, or even the entire array is zero.

Now the loop will execute until the traditional condition is true: left_idx < right_idx.

Once inside the loop we look at which value is smaller: left of right - and from there we will
calculate the water level, which I will detail the steps later. But at this point the interesting
part is to analyse how 

'''

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def trap(self, height: List[int]) -> int:
        total_water : int = 0
        
        left_idx    : int = 0
        right_idx   : int = len(height) - 1

        v_max_left  : int = height[left_idx]  # We can start from the edges and consider them max values
        v_max_right : int = height[right_idx] #  regardless of the values (being 0 or nor) the logic will work

        #-----------------------------------
        while left_idx < right_idx:
            if v_max_left <= v_max_right: 
                left_idx += 1
                
                # usual way to calculate water level
                v_left : int = height[left_idx]
                v_max_left : int = max(v_max_left, v_left) 
                curr_water : int = v_max_left - v_left 
                total_water += curr_water
            else: # max_left > max_right
                right_idx -= 1
                
                # usual way to calculate water level
                v_right : int = height[right_idx]
                v_max_right : int = max(v_max_right, v_right)
                curr_water : int = v_max_right - v_right
                total_water += curr_water
        #-----------------------------------
              
        return total_water    
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
