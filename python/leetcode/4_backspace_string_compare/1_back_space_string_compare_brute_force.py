#problem: https://leetcode.com/problems/backspace-string-compare/description/
class Solution:
    #-------------------------------------------------------------------------
    def buildString(self, s:str) -> str:
        stack = []
        #------
        for c in s:
            #------
            if c != '#':
                stack.append(c)
            else:
                if stack:
                    stack.pop()
            #------
        #------
        return ''.join(stack)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = self.buildString(s)
        new_t = self.buildString(t)

        return new_s == new_t
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    
sol = Solution()
s = "a#c"
t = "b"
expected = False
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')
