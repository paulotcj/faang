#problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


#-------------------------------------------------------------------------
class Solution: 
    #-------------------------------------------------------------------------
    def searchRange( self , nums : list[int] , target: int ) -> list[int] :
        if not nums : return [-1,-1]
        
        val_found_at_idx = self.binary_search(arr = nums, target = target )
        if val_found_at_idx == -1 : return [-1,-1]
        
        left_idx  : int = val_found_at_idx
        right_idx : int = val_found_at_idx
        #-----------------------------------
        while left_idx > 0 and nums[left_idx-1] == target :
            left_idx -= 1
        #-----------------------------------
        while right_idx < len(nums) - 1 and nums[right_idx + 1] == target :
            right_idx += 1
        #-----------------------------------
        
        return [left_idx, right_idx]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def binary_search( self , arr : list[int] , target : int ) -> int :
        left_idx : int = 0
        right_idx : int = len(arr) - 1
        
        #-----------------------------------
        while left_idx <= right_idx :
            mid_idx : int = (left_idx + right_idx) // 2
            
            #-----
            if arr[mid_idx] == target : return mid_idx
            elif arr[mid_idx] < target: left_idx += 1
            else : right_idx -= 1
            #-----
        #-----------------------------------
        return -1
    #-------------------------------------------------------------------------  
#-------------------------------------------------------------------------
   
   
   
print('----------------------------')
sol = Solution()
#        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
input = [5,6,7,7,8,8,10]
target = 5
expected = [0,0]

result = sol.searchRange(input,target)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')

   
   
print('----------------------------')
sol = Solution()
#        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
input = [2,2]
target = 2
expected = [0,1]

result = sol.searchRange(input,target)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
#        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
input = [1]
target = 1
expected = [0,0]

result = sol.searchRange(input,target)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
#        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
input = [5,7,7,8,8,10]
target = 6
expected = [-1,-1]

result = sol.searchRange(input,target)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')





print('----------------------------')
sol = Solution()
#        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
input = [5,5,7,7,8,8,10]
target = 5
expected = [0,1]

result = sol.searchRange(input,target)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
#        0 1 2 3 4 5 6 7 8 9 10 11 12 13 14
input = [5,6,7,7,8,8,10]
target = 6
expected = [1,1]

result = sol.searchRange(input,target)
print(f'Expected: {expected}')
print(f'Result  : {result}')
print(f'Is the result correct? { result == expected}')





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









