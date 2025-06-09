#problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        if target not in nums: return [-1,-1]
        #---
        first_occurrence : int = nums.index(target)
        #---
        # if you have this list: lst = [1, 2, 3, 3, 3, 4], the last occurence is at
        # idx 4. So what you do is, figure out the last_idx: 5, then how many steps
        # starting from the back until the first occurrence: 1.
        # then the math is: last_idx - steps_from_the_back = 5 - 1 = 4
        last_idx : int = len(nums) - 1
        steps_from_the_back : int = nums[::-1].index(target)  # get the steps from the back until the first occurrence
        
        second_occurrence : int = last_idx - steps_from_the_back
        #---
        
        return [first_occurrence, second_occurrence]
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





