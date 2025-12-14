#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def evalRPN(self, tokens: list[str]) -> int:
        pass
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#-------------------------------------------------------------------------
def print_result(result , expected) :
    print('------------------------------------')
    is_equal = expected == result
    if is_equal:
        status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
    else:
        status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
    print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
#-------------------------------------------------------------------------
        
#------------------------
input = ["1","2","+","3","*","4","-"]
expected = 5

sol = Solution()
result = sol.evalRPN(tokens=input)
print_result(result=result,expected=expected)




