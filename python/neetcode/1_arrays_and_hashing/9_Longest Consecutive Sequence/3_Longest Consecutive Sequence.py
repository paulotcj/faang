#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 0 : return 0
        num_set : set[int] = set(nums)
        max_streak : int = 1

        #--------------------------------------------------
        for num in num_set:
            # explanation: if num-1 is not in the set, that means num is the start of a new
            #  sequence. That sequence might be of len 1, or 999,999 it doesn't matter but
            #  because there's a gap then num must be the start of a new sequence
            #-----
            if (num-1) not in num_set : 
                curr_streak : int = 1
                #-----
                while (num + curr_streak) in num_set :
                    curr_streak += 1
                #-----
                max_streak = max(max_streak, curr_streak)
            #-----
        #--------------------------------------------------
        return max_streak
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = [-1, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
expected = 7

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

print('------------------------------------')
input = [2,20,4,10,3,4,5]
expected = 4

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [0,3,2,5,4,6,1,1]
expected = 7

sol = Solution()
result = sol.longestConsecutive(nums=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')




