#problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        first = self.find_first(nums, target)
        last = self.find_last(nums, target)
        return [first, last] 
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def find_first(self , nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        first_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                if nums[mid] == target:
                    first_pos = mid
                right = mid - 1
        return first_pos
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def find_last(self , nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        last_pos = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                if nums[mid] == target:
                    last_pos = mid
                left = mid + 1
        return last_pos
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





