# https://leetcode.com/problems/trapping-rain-water/
from typing import List

''' start with house keeping, set 'total_water' to zero, seet the left_index to 0 set the right_index
to len(height) - 1 (e.g.: 10 - 1 = 9 which is the idx of the last element in the array). And from there
we set the 'v_max_left' and 'v_max_right' according to their indexes. The difference here from the
previous approach is that we realized we don't need to care for the values of left or right, the
algorithm will sort it out if the extremeties have values of 0, or even the entire array is zero.

Now the loop will execute until the traditional condition is true: left_idx < right_idx.

Once inside the loop we look at which value is smaller: left of right - and from there we will
calculate the water level, which I will detail the steps later. 
But at this point the interesting part is to analyse how the algorithm works and solve some cases

For an array as in height = [0,0,8,3,7,2,9,0,0], the starting condition would be: 
total_water = 0,
left_idx  = 0 , left_v  = 0 , v_max_left  = 0
right_idx = 8 , right_v = 0 , v_max_right = 0

- Left index is smaller than right index so the loop executes
- v_max_left is smaller or equal than v_max_right, that means we calculate the water level based on the
    smaller 'border', in this case the left side, since this is the limiting factor
- move the left index 1 position to the right (left_idx = 1), get the value for left_v = 0
- now get the max(left_v, v_max_left) and assign this to v_max_left. This is the interesting part as if
    v_max_left had the max value already, we can intuitively see that this will form a 'well' where water
    can accumulate, if they are the same level no water can accumulate, and if this new position is an
    increase in height and in fact assumed the 'max value' then again no water will acumulate. And we don't
    care for the other wall (in this example right) because it should be bigger. And again, in the case of
    left_v being bigger than the right wall, no water would accumulate.
    
    For our specific case where both walls are 0, and the current value is zero, we can conclude that
    for both walls being 0 and the current height being 0, no water accumulation would happen, and
    therefore the algorithm still works. 
    
    And that's how the edge cases where the border are padded with zeros. You can see how this would
    work just the same with an array with only zeros, or any repeated number throughout the array.
-----

Let's explore a more conventional case. 

height = [8,3,7,2,9]
total_water = 0,
left_idx  = 0 , left_v  = 8 , v_max_left  = 8
right_idx = 4 , right_v = 9 , v_max_right = 9

- Left index is smaller than right index so the loop executes
- v_max_left is smaller or equal than v_max_right, that means we calculate the water level based on the
    smaller 'border', in this case the left side, since this is the limiting factor
- move the left index 1 position to the right (left_idx = 1), get the value for left_v = 3
- v_max_left = max(v_max_left, left_v) -> v_max_left = max(8, 3) -> v_max_left = 8
- now calculate the water level: water_level = potental_water_level - terrain_height ->
    water_level = v_max_left - left_v -> 8 - 3 = 5 -> water_level = 5 at idx 1
- the procces is identical to right, except the index movement is decreased (right_idx -= 1) since
    the movement is from right to left. Also the variables change, but that's it
    
The conclusion is that by constantly checking which 'v_max' is greater we are always comparing walls
size, and per definition we are getting updated information. The initial state doesn't need to know
anything about the inner walls. It doesn't matter if they are bigger. And then advance 1 step and
compare the height of that step with the walls and figure out how much water would've accumulated on
that spot.
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
