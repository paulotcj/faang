#problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
    
        left: int = -1
        right: int = -1
    
        for i, v in enumerate(nums):
            if v == target:
                if left == -1:
                    left = i
                    right = i
                else:
                    right = i
        
        return [left, right]
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def binary_search(self, nums:List[int], left: int, right: int, target: int) -> int:
        # if nums[left] == target: return left
        # if nums[right] == target: return right
        # print('hi')
        while left <= right:  
            midpoint: int = (right - left) // 2 + left

            midpoint_val = nums[midpoint]
            if midpoint_val == target: 
                return midpoint

            if midpoint_val < target:
                left = midpoint + 1
            else:
                right = midpoint - 1

        return -1
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def search_left(self, nums: List[int], target: int, left: int, right: int) -> int:
        # print('hi')
        while right >= left:
            temp_idx: int = self.binary_search(nums = nums, left = left, right = right, target = target)

            if temp_idx == -1: return -1 #not found
            if temp_idx == 0: return 0 #found at the beggining
            
            if nums[temp_idx - 1] == target: 
                right = temp_idx - 1 #trim array
            else:
                return temp_idx
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def search_right(self, nums: List[int], target: int, left: int, right: int) -> int:
        # print('hi')
        while right >= left:
            temp_idx = self.binary_search(nums = nums, left = left, right = right, target = target)
            
            #we don't need to worry about not found or beggining

            if (temp_idx+1) <= right and nums[temp_idx + 1 ] == target:
                left = temp_idx + 1
            else: 
                return temp_idx
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums : return [-1,-1]
        left : int = self.search_left(nums= nums, target = target, left = 0, right = len(nums) -1)
        if left == -1 : return [-1, -1] #not found
        right : int = self.search_right(nums = nums, target = target, left = left, right = len(nums)-1)

        return [left,right]
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
# print('----------------------------')
# sol = Solution()
# #        0 1 2 3 4 5 6 7  8  9  10 11 12 13
# input = [3,4,5,6,7,8,9,10,11,12,13,14,15,16]
# target = 12
# expected = 9

# result = sol.binary_search(input, 0, len(input)-1, target)
# print(f'Expected: {expected}')
# print(f'Result  : {result}')
# print(f'Is the result correct? { result == expected}')

print('----------------------------')
sol = Solution()
#        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
input = [5,7,7,8,8,10]
target = 8
expected = [3, 4]

result = sol.searchRange(input,target)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')
exit()

print('----------------------------')
sol = Solution()
#        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
input = [1,2,3,4,5,5,5,5,5,5,5, 6, 7, 8, 9]
target = 5
expected = [4, 10]

result = sol.searchRange(input, 5)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')





