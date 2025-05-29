# https://leetcode.com/problems/trapping-rain-water/
from typing import List


''' Let's start with house keeping, we get the 'len_hei' as the length of the array length,
and if 'len_hei' is zero then shortcut the algorithm and return 0.
Then the usual vriables used in most solutions for this problem:
left_idx = 0, right_idx = (len_hei  - 1), left_max_v = 0, right_max_v = 0, total_trapped_water = 0

The initial difference here is that max_values are set to zero. So in this approach the deciding 
parameters for which side will be processed (left or right) are  based on the current values of the 
left and right side as opposed to the max_values. The details are presented below.

- check if left_idx < right_idx (most common approach)
- grab the values of left_v and right_v - for simplicity
- now the trick, and how this method is different: it compares which value is the lower, left or right,
    as opposed to max_values.
    If the value from the side being inspected is bigger or equal to the max_value, it just record
    the max_value and move the index inwards. This results in fewer operations which can lead to a small
    performance gains, and a simpler approach. So continuing the explanation and for simplicity I will
    only present the process from the left side perspective, but the process is very similar on the 
    right side.
- is left_v <= right_v ? if so process the left side
- if left_v <= left_max_v: just update left_max_v (left_max_v = left_v)
- else the value of left_max_v is bigger than left_v, which means this forms a well and then it's
    possible to calculate the water level.
    One concern here is that the value of the right_max_v is not known and therefore it's counter
    intuitive to ascertain if it will form a wall or not. But the reality is that before it was checked 
    for left_v <= right_v, so there's a right wall at least as big as the left wall - considering this
    example where the left path was taken, but this would still be true if the right path was picked.
- calculate the water level: current_water = portential_water - terrain height ->
    current_water = left_max_v - left_v
- move the left_idx inwards: left_idx += 1 (for the right side: right_idx -= 1)
- repeat the loop

Let's think about some examples. All the heights are zero and no water should accumulate
  height = [0,0,0,0]
  total_trapped_water = 0
  left_idx  =  0                  , left_max_v  = 0
  right_idx = (len_hei  - 1) = 3  , right_max_v = 0
- if left_idx(0) < right_idx(3) -> true
- assign left_v = 0, right_v = 0
- if left_v(0) <= right_v(0) -> true
- if left_v(0) >= left_max_v(0) -> true
- update left_max_v = left_v(0). left_max_v is now 0
- increment left_idx -> left_idx(1)

Now it should be clear this exact cycle will repeat a few more times, and the left_idx is the one that
will keep moving inwards until it reaches right_idx, at which point the loop stops. Also the water
level is never increased, which is the desired outcome.

Another example. There's only 1 wall and no water should accumulate.
Let's think about some examples.
  height = [0,5,0,0]
  total_trapped_water = 0
  left_idx  =  0                  , left_max_v  = 0
  right_idx = (len_hei  - 1) = 3  , right_max_v = 0
  
--- loop start ---
- if left_idx(0) < right_idx(3) -> true
- assign left_v = 0 , right_v = 0
- if left_v(0) <= right_v(0) -> true   (go process the left side)
- if left_v(0) >= left_max_v(0) -> true  
- update left_max_v = left_v(0). left_max_v is now 0
- increment left_idx -> left_idx(1)
  --- loop ---
- if left_idx(1) < right_idx(3) -> true
- assign left_v = 5 , right_v = 0
- if left_v(5) <= right_v(0) -> false  (go process the right side)
- if right_v(0) >= right_max_v(0) -> true
- update right_max_v = right_v(0). right_max_v is now 0
- decrement right_idx -> right_idx(2)

And now it's clear that the left_idx will not move, and the right_idx will continue to move inwards
until the loop condition left_idx < right_idx becomes false. So no water level will be accumulated.

And finally a more traditional example. We expect the see water accumulation between the indexes 
2 and 3
  height = [0,5,1,1,8]
  total_trapped_water = 0
  left_idx  =  0                  , left_max_v  = 0
  right_idx = (len_hei  - 1) = 4  , right_max_v = 0
  
--- loop start ---
- if left_idx(0) < right_idx(4) -> true
- assign left_v = 0 , right_v = 8
- if left_v(0) <= right_v(8) -> true  (go process the left side)
- if left_v(0) >= left_max_v(0) -> true  
- update left_max_v = left_v(0). left_max_v is now 0
- increment left_idx -> left_idx(1)
--- loop ---
- if left_idx(1) < right_idx(4) -> true
- assign left_v = 5 , right_v = 8
- if left_v(5) <= right_v(8) -> true  (go process the left side)
- if left_v(5) >= left_max_v(0) -> true  
- update left_max_v = left_v(5). left_max_v is now 5
- increment left_idx -> left_idx(2)
--- loop ---
- if left_idx(2) < right_idx(4) -> true
- assign left_v = 1 , right_v = 8
- if left_v(1) <= right_v(8) -> true  (go process the left side)
- if left_v(1) >= left_max_v(0) -> false  
- current_water = potential_water - terrain_level -> current_water = left_max_v - left_v
    current_water = 5 - 1 = 4
    total_trapped_water = total_trapped_water + current_water = 0 + 4 = 4
- increment left_idx -> left_idx(3)

Since the values of the next step are identical, the water found on the next step is 4 with a total
accumulation of 8. Then eventually left_idx will be equal to right_idx, which breaks the loop
condition, and then we return the total_trapped_water
'''
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
            if left_v <= right_v:
                #----------
                if left_v >= left_max_v:
                    left_max_v : int = left_v
                else:
                    total_trapped_water += left_max_v - left_v
                #----------
                left_idx += 1
            else:
                #----------
                if right_v >= right_max_v:
                    right_max_v : int = right_v
                else:
                    total_trapped_water += right_max_v - right_v
                #----------
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
