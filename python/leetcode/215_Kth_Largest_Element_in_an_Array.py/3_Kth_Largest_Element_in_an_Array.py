#problem: https://leetcode.com/problems/kth-largest-element-in-an-array/


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums : list[int] = self.quicksort( arr = nums )
        return nums[-k]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def quicksort_inplace( self , arr : list[int] , low_idx : int = None , high_idx : int = None ) -> list[int] :
        if low_idx  is None : low_idx = 0
        if high_idx is None : high_idx = len(arr) -1
        
        #-----
        if low_idx < high_idx :
            pivot_idx : int = self.partition( arr = arr , low_idx = low_idx , high_idx = high_idx )
            
            self.quicksort_inplace( arr = arr , low_idx = low_idx , high_idx = pivot_idx - 1 ) # left subarray
            self.quicksort_inplace( arr = arr , low_idx = pivot_idx + 1 , high_idx = high_idx ) # right subarray
        #-----
        
        return arr
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def partition( self , arr : list[int] , low_idx : int , high_idx : int ) -> int :
        pivot : int = arr[high_idx] # pivot is the last element
        idx_tracking_low_val : int = low_idx - 1 # index of smaller element
        
        #-----------------------------------
        for idx_scanner in range( low_idx , high_idx ) :
            if arr[idx_scanner] < pivot :
                idx_tracking_low_val += 1
                arr[idx_tracking_low_val] , arr[idx_scanner] = arr[idx_scanner] , arr[idx_tracking_low_val]
        #-----------------------------------
        
        # swapping the pivot that is sitting at arr[high_idx] to arr[idx_tracking_low_val + 1]
        idx_tracking_low_val += 1 # let's simplify things and just move this 1 step ahead
        arr[idx_tracking_low_val] , arr[high_idx] = arr[high_idx] , arr[idx_tracking_low_val]
        return idx_tracking_low_val
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------



sol = Solution()
original_array = [5,4,3,2,1]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_inplace(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')


sol = Solution()
original_array = [1,2,3,4,5]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_inplace(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')


sol = Solution()
original_array = [1,4,5,2,3]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_inplace(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')






sol = Solution()
original_array = [2,6,5,3,8]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_inplace(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')




sol = Solution()
original_array = [3,2,3,1,2,4,5,5,6]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_inplace(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')



sol = Solution()
original_array = [37, 12, 85, 64, 23, 7, 91, 56, 48, 19, 73, 2, 41, 88, 30, 60, 15, 99, 53, 27]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_inplace(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')


