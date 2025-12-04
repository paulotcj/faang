from collections import Counter
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) : return False

        cnt_s , cnt_t = {} , {}

        #--------------------------------------------------
        for i in range( len(s) ) :
            s_val , t_val = s[i], t[i]
            cnt_s[ s_val ] = cnt_s.get( s_val , 0 ) + 1
            cnt_t[ t_val ] = cnt_t.get( t_val , 0 ) + 1
        #--------------------------------------------------

        return cnt_s == cnt_t
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
    

print('------------------------------------')
input1 = "racecar"
input2 = "carrace"
expected = True

sol = Solution()
result = sol.isAnagram(s=input1, t = input2)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')



print('------------------------------------')
input1 = "jar"
input2 = "jam"
expected = False

sol = Solution()
result = sol.isAnagram(s=input1, t = input2)
print(f'is the result what was expected? {expected == result} - expected: {expected} - result : {result}')