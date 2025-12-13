

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def hasDuplicate(self, nums: list[int]) -> bool:

        #--------------------------------------------------
        for i in range( len(nums) ) : # loop throuh the array, but anchor the comparisson at position i
            #-----
            for j in range(i+1, len(nums) ) : # now go checking for every new position after i
                if nums[i] == nums[j] : # found the same value
                    return True
            #-----
        #--------------------------------------------------
        return False

    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('------------------------------------')
input = [1, 2, 3, 4]
expected = False

sol = Solution()
result = sol.hasDuplicate(nums=input)


is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = [1, 2, 3, 3]
expected = True

sol = Solution()
result = sol.hasDuplicate(nums=input)


is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')