from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        temp_dict: defaultdict[str, list[str]] = defaultdict(list)  # create a default dict with a default value of a list
        #--------------------------------------------------
        for loop_str in strs:
            temp_sorted_str: str = ''.join(sorted(loop_str))  # make a sorted version of the loop string
            temp_dict[temp_sorted_str].append(loop_str)  # make the sorted version the dict key, and append the sorted string to the list
        #--------------------------------------------------

        return_obj: list[list[str]] = list(temp_dict.values())  # convert the dict values to a list of lists
        return return_obj  # now we have all the anagram pairs combined in lists inside a list
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = ["act","pots","tops","cat","stop","hat"]
expected = [["hat"],["act", "cat"],["stop", "pots", "tops"]]

sol = Solution()
result = sol.groupAnagrams(strs=input)

expected = sorted([sorted(inner) for inner in expected])
result = sorted([sorted(inner) for inner in result])
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = ["x"]
expected = [["x"]]

sol = Solution()
result = sol.groupAnagrams(strs=input)
expected = sorted([sorted(inner) for inner in expected])
result = sorted([sorted(inner) for inner in result])
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [""]
expected = [[""]]

sol = Solution()
result = sol.groupAnagrams(strs=input)
expected = sorted([sorted(inner) for inner in expected])
result = sorted([sorted(inner) for inner in result])
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')