#-------------------------------------------------------------------------
import enum


class Solution:
    #-------------------------------------------------------------------------
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        return_obj : list[int] = [0] * len(nums)

        #-----
        for i_idx , i_val_donotuse in enumerate(nums):
            temp_prod : int = 1
            #-----
            for j_idx , j_val in enumerate(nums):
                if i_idx != j_idx :
                    temp_prod *= j_val
            #-----
            return_obj[i_idx] = temp_prod
        #-----

        return return_obj
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = [1,2,4,6]
expected = [48,24,12,8]

sol = Solution()
result = sol.productExceptSelf(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input =    [-1, 0, 1, 2, 3]
expected = [ 0,-6, 0, 0, 0]

sol = Solution()
result = sol.productExceptSelf(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')