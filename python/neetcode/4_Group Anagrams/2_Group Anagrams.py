from collections import defaultdict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        res : defaultdict[int] = defaultdict( list )

        #--------------------------------------------------
        for loop_str in strs :
            count : list[int] = [0] * 26 # creates a list with 26 zeroes
            #-----
            for char in loop_str :

                # we are basically trying to shift the unicode value of this string into a zero based alphabet array
                char_idx : int = ord(char) - ord('a') # ord -> return the unicode value of a single char string
                count[ char_idx ] += 1 # increment the count value
            #-----
            
            dict_key_tuple = tuple(count) #after this pre-processing any anagram would be sorted in the same fashion resulting in the same key
            res[ dict_key_tuple ].append( loop_str ) #then we can group them together by using the same key
        #--------------------------------------------------

        return list( res.values() )



    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')
input = ["act","pots","tops","cat","stop","hat"]
expected = [["hat"],["act", "cat"],["stop", "pots", "tops"]]

sol = Solution()
result = sol.groupAnagrams(strs=input)

expected = sorted([sorted(inner) for inner in expected])
result = sorted([sorted(inner) for inner in result])
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')



print('------------------------------------')
input = ["x"]
expected = [["x"]]

sol = Solution()
result = sol.groupAnagrams(strs=input)
expected = sorted([sorted(inner) for inner in expected])
result = sorted([sorted(inner) for inner in result])
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = [""]
expected = [[""]]

sol = Solution()
result = sol.groupAnagrams(strs=input)
expected = sorted([sorted(inner) for inner in expected])
result = sorted([sorted(inner) for inner in result])
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')