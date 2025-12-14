#-------------------------------------------------------------------------
class Solution:
    # Note: This implementation is not true RPN as it evaluates expressions more like
    #  as in assembly than RPN
    #-------------------------------------------------------------------------
    def evalRPN(self, tokens: list[str]) -> int:
        len_tokens = len(tokens)
        if len_tokens == 1 : return int(tokens[0]) # no operation to be done
        elif len_tokens < 3 : return None # cover the cases of len 0 and 2 where there's no possible operation 
        # len_token == 3 it's ok
        elif len_tokens > 3 and ((len_tokens - 3) % 2) != 0 : # we expect 3 initial tokens, and then they should come in pairs
            return None
        
        a : int = None
        b : int = None
        operator : str = None

        #--------------------------------------------------
        for s in tokens:
            #-----
            if a == None : 
                a = int(s)
                continue
            elif b == None : 
                b = int(s)
                continue
            elif operator == None : 
                operator = s
            
                #-----
                if operator == "+" : 
                    a = a+b
                elif operator == "-" :
                    a = a-b
                elif operator == "*" :
                    a = a*b
                elif operator == "/" :
                    a = int(a/b)
                else :
                    print('error at identifying operator')
                #-----
                b = None
                operator = None
            #-----
        #--------------------------------------------------


        return a
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




