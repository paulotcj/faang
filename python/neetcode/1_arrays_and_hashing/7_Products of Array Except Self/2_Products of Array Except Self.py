#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        zero_cnt : int = 0
        total_prod : int = 1
        #-----
        for num in nums : 
            if num == 0 : zero_cnt += 1
            else : total_prod *= num
        #-----

        return_obj : list[int] = [0] * len(nums)
        if zero_cnt > 1 : return return_obj

   
        #-----
        for idx, val in enumerate(nums):
            # if we do have a zero val in the array, and this is not the zero
            #   val, then the product in this position must be zero
            if zero_cnt: return_obj[idx] = 0 if val != 0 else total_prod
            else: return_obj[idx] = total_prod // val
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
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input =    [-1, 0, 1, 2, 3]
expected = [ 0,-6, 0, 0, 0]

sol = Solution()
result = sol.productExceptSelf(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')