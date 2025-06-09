#problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/


#-------------------------------------------------------------------------
class Solution: 
    #-------------------------------------------------------------------------
    def searchRange( self , nums : list[int] , target: int ) -> list[int] :
        if not nums : return [-1,-1]
        len_nums : int = len(nums)
        if len_nums == 1 and nums[0] == target: return [0,0]
        
        val_found_at_idx = self.binary_search(arr = nums, target = target)
        if val_found_at_idx == -1: return [-1,-1] # value not found
        
        left_bound_idx : int = val_found_at_idx
        right_bound_idx : int = val_found_at_idx
        
        #-----------------------------------
        while left_bound_idx > 0 :
            if nums[left_bound_idx-1] == target: left_bound_idx -= 1
            else: break
        #-----------------------------------
        while right_bound_idx < len_nums - 1 :
            if nums[right_bound_idx+1] == target : right_bound_idx += 1
            else: break
        #-----------------------------------
        
        return [left_bound_idx, right_bound_idx] 
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def binary_search( self , arr : list[int] , target : int ) -> int:
        left_idx : int = 0
        right_idx : int = len(arr) - 1
        mid_point_idx : int = (right_idx - left_idx) // 2
        prev_midpoint : int = None
        
        #-----------------------------------
        while left_idx < right_idx:
            if arr[mid_point_idx] == target:
                return mid_point_idx
            
            if arr[mid_point_idx] < target :
                left_idx = mid_point_idx 
                step : int = max((right_idx - left_idx) // 2 , 1)
                temp_mid_point : int = mid_point_idx + step
                
            else: # arr[mid_point_idx] > target
                right_idx = mid_point_idx
                step : int = max((right_idx - left_idx) // 2, 1)
                temp_mid_point : int = mid_point_idx - step
                
            if prev_midpoint == temp_mid_point : return -1 # this prevents infinite loops for values non existent in the array
            else: 
                prev_midpoint = mid_point_idx
                mid_point_idx = temp_mid_point
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









