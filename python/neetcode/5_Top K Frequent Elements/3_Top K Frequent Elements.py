from collections import defaultdict
import heapq
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        pass

        #--------------------------------------------------

        #--------------------------------------------------


        #--------------------------------------------------

        #--------------------------------------------------  


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
        

print('------------------------------------')
input = [1,2,2,3,3,3]
input_aux = 2
expected = [2,3]

sol = Solution()
result = sol.topKFrequent(nums=input, k=input_aux)
expected.sort()
result.sort()

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [7,7]
input_aux = 1
expected = [7]

sol = Solution()
result = sol.topKFrequent(nums=input, k=input_aux)
expected.sort()
result.sort()

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = [1,1,1,2,2,3]
input_aux = 2
expected = [1,2]

sol = Solution()
result = sol.topKFrequent(nums=input, k=input_aux)
expected.sort()
result.sort()

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')