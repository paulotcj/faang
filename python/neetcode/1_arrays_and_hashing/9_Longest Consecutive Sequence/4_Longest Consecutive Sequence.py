from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def longestConsecutive(self, nums: list[int]) -> int:
        
        seq_map = defaultdict(lambda: 0)
        max_streak : int = 0

        #--------------------------------------------------
        for num in nums:
            #-----
            if seq_map[num] == 0: # we only want elements we haven't looked at
                # if the neighbours are all zero, then there's no difference, but if the previous
                #  one has a streak we need that, and if the next number was placed out of sequence
                # we need to know it's streak too, as it might be 0, might be 1, maybe 99, but then
                # we merge: 'previous streak', + 1 from this number + next number known streak
                prev_streak     : int = seq_map[num - 1] 
                next_streak     : int = seq_map[num + 1]
                current_streak  : int = prev_streak + next_streak + 1 # merge all streaks
                seq_map[num] = current_streak

                # now go back to where all streaks started and update this number
                start_streak_loc : int = num - prev_streak 
                seq_map[ start_streak_loc] = current_streak

                #and also go to the end of the streak and update its numbers
                end_streak_loc : int = num + next_streak
                seq_map[end_streak_loc] = current_streak

                max_streak = max(max_streak, current_streak)
            #-----
        #--------------------------------------------------
        return max_streak
    #-------------------------------------------------------------------------    
#-------------------------------------------------------------------------

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




