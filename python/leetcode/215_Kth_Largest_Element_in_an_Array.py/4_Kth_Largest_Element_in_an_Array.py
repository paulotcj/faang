#problem: https://leetcode.com/problems/kth-largest-element-in-an-array/


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums : list[int] = self.quicksort( arr = nums )
        return nums[-k]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def quicksort_iterative(self , arr : list[int]):
        # Create an explicit stack for holding (low, high) index pairs
        stack : list[int] = []

        # Push initial bounds of the array
        stack.append((0, len(arr) - 1))

        # Loop until stack is empty
        #-----------------------------------
        while stack:
            low, high = stack.pop()

            if low < high:
                # Partition the array and get the pivot index
                pivot_index = self.partition(arr, low, high)

                # Push subarrays to stack
                stack.append((low, pivot_index - 1))   # left subarray
                stack.append((pivot_index + 1, high))  # right subarray
        #-----------------------------------
        
        return arr
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def partition(self , arr : list[int] , low : int , high : int ):
        pivot : int = arr[high]
        i : int = low - 1

        #-----------------------------------
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i] , arr[j] = arr[j] , arr[i]  # Swap smaller element to left side
        #-----------------------------------

        arr[i + 1] , arr[high] = arr[high] , arr[i + 1]  # Move pivot to its correct position
        return i + 1
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
original_array = [3,2,3,1,2,4,5,5,6]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_iterative(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')
# exit()


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
original_array = [37, 12, 85, 64, 23, 7, 91, 56, 48, 19, 73, 2, 41, 88, 30, 60, 15, 99, 53, 27]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_iterative(arr = original_array)
print(f'expected: {expected}')
print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')


