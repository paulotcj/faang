#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        arr_map : dict[int,int] = {}

        #--------------------------------------------------
        for idx , num in enumerate(nums) :
            diff = target - num
            #----
            if diff in arr_map:
                # just rearrange how we display the indexes as the solution expects the lower index to be shown
                #  first, and it just so happens to be what is stored in the arr_map
                return [ arr_map[diff] , idx ]
            #----
            arr_map[num] = idx
        #--------------------------------------------------

        return []
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
        
print('------------------------------------')
input = [3,4,5,6]
target = 7
expected = [0,1]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [4,5,6]
target = 10
expected = [0,2]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = [5,5]
target = 10
expected = [0,1]

sol = Solution()
result = sol.twoSum(nums=input , target=target)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')