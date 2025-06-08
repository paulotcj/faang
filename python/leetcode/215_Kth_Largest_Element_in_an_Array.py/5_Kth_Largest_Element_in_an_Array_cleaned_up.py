#problem: https://leetcode.com/problems/kth-largest-element-in-an-array/


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums : list[int] = self.quicksort_iterative( arr = nums )
        return nums[-k]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def quicksort_iterative(self , arr : list[int]):
        # Create an explicit stack for holding (low, high) index pairs
        stack : list[int] = []

        # Push initial bounds of the array
        stack.append((0, len(arr) - 1)) # low_idx, high_idx

        # Loop until stack is empty
        #-----------------------------------
        while stack:
            low_idx, high_idx = stack.pop() # only added pivot_index for educational purposes


            if low_idx < high_idx: 
                # Partition the array and get the pivot index
                pivot_index = self.partition(arr, low_idx, high_idx)

                #-----
                # pivot is already in place, now it's necessary to investigate the subarrays to the
                #  left and to the right, while excluding pivot's place
                pivots_left  : int = pivot_index - 1
                pivots_right : int = pivot_index + 1
                left_subarray_range  : tuple[int,int] = (low_idx, pivots_left)   
                right_subarray_range : tuple[int,int] = (pivots_right, high_idx)
                
                stack.append(left_subarray_range)   # left subarray range
                stack.append(right_subarray_range)  # right subarray range
                
        #-----------------------------------
        
        return arr
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def partition(self , arr : list[int] , low_idx : int , high_idx : int ):
        pivot : int = arr[high_idx]

        # idx i is meant to track and swap values to the left, values smaller than the pivot
        idx_tracking_low_val : int = low_idx - 1  

        #-----------------------------------
        for idx_scanner in range(low_idx, high_idx): 
            if arr[idx_scanner] <= pivot: # is this value meant to be swapped to the left?
                
                idx_tracking_low_val += 1 # move the pointer 1 step ahead
                arr[idx_tracking_low_val] , arr[idx_scanner] = arr[idx_scanner] , arr[idx_tracking_low_val]  # Swap smaller element to left side
        #-----------------------------------

        # Move pivot to its correct position
        arr[idx_tracking_low_val + 1] , arr[high_idx] = arr[high_idx] , arr[idx_tracking_low_val + 1]  
        return idx_tracking_low_val + 1
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


