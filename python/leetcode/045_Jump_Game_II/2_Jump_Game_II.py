#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def jump(self, nums: list[int]) -> int:
        len_nums : int = len(nums)
        index : int = 0
        jumps : int = 0

        #----------------------------------------
        while index < len_nums-1:
            if index + nums[index] >= len_nums - 1:
                jumps += 1
                break

            longest : int = -1
            next_ind : int = 0
        
            #----------------------------------------
            for i in range(index+1, min(nums[index]+1+index, len_nums)):
                if i + nums[i] > longest:
                    longest : int = nums[i] + i
                    next_ind : int = i
            #----------------------------------------

            jumps += 1
            index = next_ind
        #----------------------------------------
        
        return jumps
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
input = [2,3,1,1,4]
expected_result = 2
result = sol.jump(nums = input)
print(f'result: {result} - expected: {expected_result} - is the result expected?: {result==expected_result}')
print('-----')

sol = Solution()
input = [2,3,0,1,4]
expected_result = 2
result = sol.jump(nums = input)
print(f'result: {result} - expected: {expected_result} - is the result expected?: {result==expected_result}')
print('-----')


