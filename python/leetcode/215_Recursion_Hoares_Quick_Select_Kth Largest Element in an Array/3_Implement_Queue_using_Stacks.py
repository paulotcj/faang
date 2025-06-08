#problem: https://leetcode.com/problems/kth-largest-element-in-an-array/


#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums : list[int] = self.quicksort( arr = nums )
        return nums[-k]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def quicksort_inplace(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quicksort_inplace(arr, low, pi - 1)
            self.quicksort_inplace(arr, pi + 1, high)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def partition(self, arr, low, high):
        pivot = arr[high]  # pivot is the last element
        i = low - 1  # index of smaller element

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # swap

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # swap pivot into correct position
        return i + 1  
    #-------------------------------------------------------------------------  
#-------------------------------------------------------------------------

sol = Solution()
original_array = [3,2,3,1,2,4,5,5,6]

expected = original_array.copy()
expected.sort()
result = sol.quicksort_inplace(arr = original_array , low = 0 , high = len(original_array) - 1)
# print(f'expected: {expected}')
# print(f'result  : {result}')
print(f'Is the result correct? { result == expected}')

print('------------------')
# exit()


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


