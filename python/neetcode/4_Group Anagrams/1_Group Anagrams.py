from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        temp_dict = defaultdict( list ) # create a default dict with a default value of a list
        #--------------------------------------------------
        for loop_str in strs :
            temp_sorted_str = ''.join( sorted(loop_str) ) # make a sorted version of the loop string
            temp_dict[temp_sorted_str].append(loop_str) # make the sorted version the dict key, and append the sorted string to the list
        #--------------------------------------------------

        return_obj : list[list[str]] = list( temp_dict ) # convert the dict in a list
        return  return_obj # now we have all the anagram pairs combined in lists inside a list
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = ["act","pots","tops","cat","stop","hat"]
expected = [["hat"],["act", "cat"],["stop", "pots", "tops"]]

sol = Solution()
result = sol.groupAnagrams(strs=input)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = ["x"]
expected = [["x"]]

sol = Solution()
result = sol.groupAnagrams(strs=input)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [""]
expected = [[""]]

sol = Solution()
result = sol.groupAnagrams(strs=input)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')