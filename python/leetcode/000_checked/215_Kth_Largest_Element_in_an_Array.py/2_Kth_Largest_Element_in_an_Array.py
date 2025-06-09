#problem: https://leetcode.com/problems/kth-largest-element-in-an-array/


#-------------------------------------------------------------------------
class Solution : 
    #-------------------------------------------------------------------------
    def findKthLargest( self , nums : list[int] , k : int ) -> int :
        nums : list[int] = self.quicksort( arr = nums )
        return nums[-k]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def quicksort( self , arr : list[int] ) -> list[int] :
        if len(arr) <= 1 : return arr # base case: already sorted
        
        pivot : int = arr[0]
        
        left   : list[int] = [ x for x in arr if x <  pivot ] # smaller than pivot
        middle : list[int] = [ x for x in arr if x == pivot ] # for cases where there are move values equal to pivot
        right  : list[int] = [ x for x in arr if x >  pivot ] # greater than pivot
        
        return_result : list[int] = self.quicksort( arr = left ) + middle + self.quicksort(arr = right)
        
        return return_result
    #-------------------------------------------------------------------------   
#-------------------------------------------------------------------------

sol = Solution()
original_array = [3,2,3,1,2,4,5,5,6]

expected = original_array.copy()
expected.sort()
result = sol.quicksort(original_array)
# print(f'expected: {expected}')
# print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')


sol = Solution()
original_array = [2,6,5,3,8]

expected = original_array.copy()
expected.sort()
result = sol.quicksort(original_array)
print(f'Is the result correct? { result == expected}')

print('------------------')



sol = Solution()
original_array = [37, 12, 85, 64, 23, 7, 91, 56, 48, 19, 73, 2, 41, 88, 30, 60, 15, 99, 53, 27]

expected = original_array.copy()
expected.sort()
result = sol.quicksort(original_array)
print(f'Is the result correct? { result == expected}')

print('------------------')


