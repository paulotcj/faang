#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValid(self, s: str) -> bool:
        dict_closing_pairs : dict[str,str] = { ')':'(' ,  ']':'[' ,  '}':'{'    }
        stack : list[str] = []

        #--------------------------------------------------
        for char in s :
            if char in dict_closing_pairs : # closing char
                if not stack : return False

                char_pop = stack.pop()

                if char_pop == dict_closing_pairs[char] : continue # pair matched
                else: return False # pair didn't match
            else: # opening char
                stack.append(char)
        #--------------------------------------------------

        return len(stack) == 0
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

print('------------------------------------')
input = "([{}])"
expected = True

sol = Solution()
result = sol.isValid(s=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


print('------------------------------------')
input = "[]"
expected = True

sol = Solution()
result = sol.isValid(s=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')




print('------------------------------------')
input = "[(])"
expected = False

sol = Solution()
result = sol.isValid(s=input)
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


        