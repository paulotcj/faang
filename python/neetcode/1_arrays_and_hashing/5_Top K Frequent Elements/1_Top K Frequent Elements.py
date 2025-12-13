from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count_dict : defaultdict[int,int] = defaultdict( lambda:0 ) # produces 0 as default
        #--------------------------------------------------
        for num in nums : 
            count_dict[num] += 1
        #--------------------------------------------------

        arr: list[list[int]] = []
        #--------------------------------------------------
        for num , count in  count_dict.items():
            arr.append( [count, num] )
        #--------------------------------------------------  
        arr.sort(reverse=True) # sort in place

        arr : list[int] = [ sublist[1] for sublist in arr[:k] ]
        return arr

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
    status_result = f"\033[1;97;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{expected == result}\033[0m"  # Bold, white text, red background
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
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
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
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')