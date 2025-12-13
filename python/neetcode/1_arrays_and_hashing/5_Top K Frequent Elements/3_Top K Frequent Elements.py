from collections import defaultdict

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        #--------------------------------------------------
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        #--------------------------------------------------
        #--------------------------------------------------            
        for num, cnt in count.items(): # now transfer the dict to a map of frequency per numbers list
            freq[cnt].append(num)
        #--------------------------------------------------
        print(freq)
        # exit()
        res = []
        #--------------------------------------------------
        for idx in reversed(range(1, len(freq))):
            print(f'idx:{idx}')
            for num in freq[idx]: # for all the numbers in this frequency bucket...
                res.append(num) # add to the response
                if len(res) == k:
                    return res
        #--------------------------------------------------
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------                
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count : defaultdict = defaultdict(lambda:0)
        freq : list[int] = [0] * (len(nums) + 1) 
        #--------------------------------------------------
        for num in nums : 
            count[num] += 1
        #--------------------------------------------------

        #--------------------------------------------------
        for num , cnt in count.items() : # now transfer the dict to a map of frequency per numbers list
            freq[cnt] = num
        #--------------------------------------------------  

        # loop in reverse order (since we are looking for the highest incidence number count) and add to the response list
        #  if there's an actual count. Then you slice it getting only the top k numbers with the highest count
        return_obj : list[int] = [ 
            num for num in freq[::-1] 
            if num > 0
        ][:k]

        return return_obj
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