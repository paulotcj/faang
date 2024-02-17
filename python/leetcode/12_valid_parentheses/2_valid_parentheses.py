#problem: https://leetcode.com/problems/valid-parentheses/description/

from typing import List, Dict
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isValid(self, s: str) -> bool:
        char_stack : List[str] = []
        dict_opening : Dict[str:str] = { '(': ')', '{': '}', '[': ']'  }
        dict_closing : Dict[str:str] = { ')': '(', '}': '{', ']': '['  }

        for c in s:
            if c in dict_opening.keys():
                char_stack.append(c)
                continue
            
            if not char_stack: #closing bracket without an opening bracket
                return False
                
            temp:str = char_stack[-1] #potentially (, {, or [
            if temp == dict_closing[c]:
                char_stack.pop()
            else:
                return False

        
        return True if not char_stack else False
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
print('----------------------------')
sol = Solution()
s = "()[]{}"
expected = True
result = sol.isValid(s)
# print(f'expected: {expected}')
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
print('----------------------------')
sol = Solution()
s = "()[{}"
expected = False
result = sol.isValid(s)
# print(f'expected: {expected}')
# print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
