#problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def searchRange( self , nums : list[int] , target : int ) -> list[int] :
        left_idx : int = -1
        right_idx : int = -1
        
        #-----------------------------------
        for loop_idx, loop_val in enumerate(nums):
            
            if loop_val == target:
                #-----
                if left_idx == -1: # found the first match...
                    left_idx = loop_idx  # set both indexes to where the first occurence starts
                    right_idx = loop_idx
                else: # this is no longer he first match, now only set the right pointer
                    right_idx = loop_idx
                #-----
        #-----------------------------------
        return [left_idx, right_idx]
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





