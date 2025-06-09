#problem: https://leetcode.com/problems/kth-largest-element-in-an-array/


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums : list[int] = self.quicksort_iterative( arr = nums )
        return nums[-k]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def quicksort_iterative( self , arr : list[int] ) -> list[int] :
        self.arr : list[int] = arr
        len_arr : int = len(arr)

        if len_arr <= 1 : return arr # base case: already sorted
        
        stack : list[tuple[int, int]] = [] # Create an explicit stack for holding (low, high) index pairs        
        stack.append( (0, len_arr - 1) ) # Push initial bounds of the array - low_idx, high_idx
        
        # Loop until stack is empty
        #-----------------------------------
        while stack :
            low_idx , high_idx = stack.pop()
            
            if low_idx < high_idx :
                pivot_idx : int = self.partition(low_idx = low_idx , high_idx = high_idx ) # Partition the array and get the pivot index
                
                # at this point pivot is already in place, now it's necessary to investigate the 
                #  subarrays to the left and to the right, while excluding pivot's place
                pivots_left  : int = pivot_idx - 1
                pivots_right : int = pivot_idx + 1
                left_subarray_range  : tuple[int, int] = (low_idx, pivots_left)
                right_subarray_range : tuple[int, int] = (pivots_right, high_idx)
                
                stack.append(left_subarray_range)
                stack.append(right_subarray_range)
        #-----------------------------------
        return arr
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def partition( self , low_idx : int , high_idx : int ) -> int :
        arr : list[int] = self.arr
        pivot : int = arr[high_idx]

        idx_tracking_low_val : int = low_idx - 1 # this idx meant to track and swap values to the left, values smaller than the pivot
        
        #-----------------------------------
        for idx_scanner in range(low_idx , high_idx) :
            #-----
            if arr[idx_scanner] <= pivot : # this value should be swapped to the left
                
                idx_tracking_low_val += 1
                arr[idx_tracking_low_val] , arr[idx_scanner] = arr[idx_scanner] , arr[idx_tracking_low_val]
            #-----
        #-----------------------------------
        
        # Move pivot to its correct position
        idx_tracking_low_val += 1 # this operation repeats a little here, let's make it simple
        arr[idx_tracking_low_val] , arr[high_idx] = arr[high_idx] , arr[idx_tracking_low_val]
        
        return idx_tracking_low_val
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
original_array = [5,4,3,2,1]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_iterative(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')


sol = Solution()
original_array = [1,2,3,4,5]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_iterative(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')


sol = Solution()
original_array = [1,4,5,2,3]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_iterative(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')






sol = Solution()
original_array = [2,6,5,3,8]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_iterative(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')




sol = Solution()
original_array = [3,2,3,1,2,4,5,5,6]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_iterative(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')



sol = Solution()
original_array = [37, 12, 85, 64, 23, 7, 91, 56, 48, 19, 73, 2, 41, 88, 30, 60, 15, 99, 53, 27]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_iterative(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')


