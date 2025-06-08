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
        stack.append((0, len(arr) - 1, len(arr) - 1)) # low_idx, high_idx, pivot_idx

        # Loop until stack is empty
        #-----------------------------------
        while stack:
            low_idx, high_idx, pivot_index = stack.pop() # only added pivot_index for educational purposes

            ''' there could be a few reasons why low_idx is bigger than high_idx. One of them is if
            the pivot's place is at the end of the array (or subarray), and then you want to slice a 
            subarray to the right of that. So the operation would be: 
            (low_idx, high_idx) = (pivot_index + 1 , high_idx)
            as we can see, the low_idx would fall of the range, since pivot_index is at the end of the
            array
            
            Another one would be if the pivot's place is at the beginning of the array (or subarray), 
            in this case you are trying to slice an array to the left of the beginning, effectively the
            low_idx would be: 
            (low_idx, high_idx) = (low_idx, pivot_index - 1) -> (low_idx, - 1) 
            in this case high_idx falls off the range, but still it would be smaller than low_idx 
            '''
            if low_idx < high_idx: 
                # Partition the array and get the pivot index
                pivot_index = self.partition(arr, low_idx, high_idx)

                #-----
                # pivot is already in place, now it's necessary to investigate the subarrays to the
                #  left and to the right, while excluding pivot's place
                pivots_left  : int = pivot_index - 1
                pivots_right : int = pivot_index + 1
                left_subarray_range  : tuple[int,int, int] = (low_idx, pivots_left, pivot_index)   
                right_subarray_range : tuple[int,int, int] = (pivots_right, high_idx, pivot_index)
                
                stack.append(left_subarray_range)   # left subarray range
                stack.append(right_subarray_range)  # right subarray range
                
                if low_idx > pivots_left:
                    print(f'  low_idx: {low_idx}\tpivots_left:{pivots_left}\tpivot_index:{pivot_index}')
                    print(f'  arr:{arr}')
                    print('  *************')
                    input("Press Enter to continue...")
                if pivots_right > high_idx:
                    print(f'  pivots_right:{pivots_right}\thigh_idx:{high_idx}\tpivot_index:{pivot_index}')
                    print(f'  arr:{arr}')
                    print('  *************')
                    input("Press Enter to continue...")
                #-----
            # else:
            #     print('debug')
        #-----------------------------------
        
        return arr
    #-------------------------------------------------------------------------
    ''' the logic here is that we are going to look at this array (or subarray) and try to put
    numbers smaller than our pivot to the left, numbers bigger than our pivot to the right.
    The goal is to find the right place for the pivot, the subarray to the left will be smaller
    than pivot, and the subarray to the right will be bigger, but we don't care if they are sorted,
    or at least not at this point.
    The algorithm will loop through the elements of this array, except the last element, which is 
    the pivot. idx_scanner gives us a hint this idx will look at every value in the range. 
    it will compare: if arr[idx_scanner] <= pivot . If this is true it means we found a number that
    is lower or equal to our pivot point, and we want to send it to the left side. And this is
    where idx_tracking_low_val enters (idx_tracking_low_val starts with the value of -1).
    We will move idx_tracking_low_val to 1 step ahead, and swap the values between 
    arr[idx_tracking_low_val] and arr[idx_scanner]. 
    This operation achived 2 things: 1 - idx_tracking_low_val is keeping track of the idx of the
    last lower than the pivot value in the array, and; 2 - we move the lower value to the left side
    Then at the end, the pivot is swapped. Pivot is sitting at arr[high_idx] - so we swap it with
    the value at arr[idx_tracking_low_val + 1], like this:
    arr[idx_tracking_low_val + 1] , arr[high_idx] = arr[high_idx] , arr[idx_tracking_low_val + 1]
    
    Now the concern about the 3 general cases:
    1 - all values are bigger than pivot. In this case nothing is swapped in the loop, we only 
        need to swap pivot with the position ahead of idx_tracking_low_val, which at this time is -1,
        so pivot will be placed at idx 0, as it should be
    2 - all values are smaller than pivot. In this case per loop logic, idx_tracking_low_val will
        follow the value of idx_scanner, so the swap operation occurs, but it's swapping the same
        position, i.e.: values from idx 4 to values of idx 4. And in the end idx_tracking_low_val is
        pointing to 1 position before the pivot, but because of this final swapping operation:
        arr[idx_tracking_low_val + 1] , arr[high_idx] = arr[high_idx] , arr[idx_tracking_low_val + 1]
        we are again swapping things ftom the same position, so nothing happens.
    3 - the array has items smaller and bigger than the pivot. In this case the array is scanned by
        idx_scanner, if the value being inspected is smaller than pivot, then this value is swapped
        by whatever is 1 step ahead of idx_tracking_low_val. Effectively idx_tracking_low_val receives
        the lower value, and is keeping track of them. And then at the end, pivot which is sitting at
        high_idx is swapped by whatever is sitting at idx_tracking_low_val+1. And then we update
        idx_tracking_low_val = idx_tracking_low_val + 1
    '''
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
exit()

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


