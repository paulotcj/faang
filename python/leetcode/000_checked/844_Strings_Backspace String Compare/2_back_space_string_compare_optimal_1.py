#problem: https://leetcode.com/problems/backspace-string-compare/description/

from typing import Tuple

''' start by comparing the strings from the end, since it might produce a quicker result if we start
to compare potential mismatchs from the end - if you start comparing by the begining you never know
how many backspaces are in front of you, in which case even if you see a valid first char you will
need to process the entire string in order to be sure. But if you have [...,a,c,#,d] you would know
for a fact that the first char is 'd' and if the second array is [....,z] then you can stop right
there.

Continuing: 
- start by comparing from the end. 
- continue to do so while the indexes are bigger than zero. At the end of each loop decrement the
    indexes. Note that is possible for empty arrays, or with too many backspaces that one index
    might become less than zero before its counterpart, but it's necessary to need to keep looking 
    because if these 2 arrays were provided: s = [#,#,a,#,#,#] and t = [a,#] - they are both
    equivalent, but 't' will run out of chars to compare first, and we need to continue to process 
    's'  
- now get the first valid char and its index. This part will move the index in accord with the 
    required number of backspaces to produce the first valid char. 
    If upon calling the function the immediate first char is valid, then the index is not moved.
    But if a backspace is present, the index will be moved -1 as per backspace, and an additional
    -1 per valid character, or until the index is bigger or equal to 0.
    For instance, if 3 backspaces needed to be processed then the index will be moved: -3 for all
    3 backspaces (-1 per backspace), and an additional -3 for 3 chars (-1 per backspace), or until 
    the index is bigger or equal to 0.
    At the end, if no valid char was found, return the index and the char as ''
    
- now compare the 2 valid chars returned. If they are not the same, it's safe to return False.

- If they are the same we need to continue to process both arrays until we find they are entirely
   the same or a mismatch. Note that it might be possible that one array may end before its
   counterpart, this case was covered above, as one array will then continue to return (-1,'')
   but it's necessary to continue to process the second array.
   
- After breaking from the loop condition: idx_s >= 0 or idx_t >= 0 - and if no mismatch was found
    then return True


'''

#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def backspaceCompare(self, s: str, t: str) -> bool:
        idx_s : int = len(s) - 1
        idx_t : int = len(t) - 1
        
        #-----------------------------------
        while idx_s >= 0 or idx_t >= 0:
            
            # get the next valid chars - if idx < 0 then '' is returned as a char
            idx_s , s_char = self.get_next_valid_char(input_str = s, idx = idx_s)
            idx_t , t_char = self.get_next_valid_char(input_str = t, idx = idx_t)
            
            if s_char != t_char : return False
            
            # we need to move the indexes becaue 'get_next_valid_char' only points to the
            #   next valid char. If you have a bunch of backspaces to process then it will
            #   reposition the indexes, but if the next char is valid it won't move the
            #   indexes
            idx_s -= 1
            idx_t -= 1
        #-----------------------------------
        
        return True
    #-------------------------------------------------------------------------  
    #------------------------------------------------------------------------- 
    def get_next_valid_char(self, input_str : str, idx : int) -> Tuple[int, str]: # get the first valid char and its index
        
        # starting with 1 because we are always going back at least 1 char
        back_space_count : int = 1 
        
        #-----------------------------------
        while idx >= 0 and back_space_count > 0:
            #------------
            if input_str[idx] == '#' : 
                back_space_count += 1
            else:
                back_space_count -= 1
                # we know it's a char but we might need to clear the backspace. If we
                # run out of chars and there's a pile of leftover backspaces, that's ok
                # but if we have lots of backspaces we need to clear all the available
                # chars
                if back_space_count == 0:
                    return (idx, input_str[idx])    
            #------------        
            idx -= 1 # no valid char or accumulated backspaces
        #-----------------------------------
        
        # at this point we we might be at idx = -1
        return (idx, '')
    #-------------------------------------------------------------------------  
#-------------------------------------------------------------------------

print('----------------------------')
sol = Solution()
s = "a"
t = "aa#a"
expected = False
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "nzp#o#g"
t = "b#nzp#o#g"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')  


print('----------------------------')
sol = Solution()
s = "bbbextm"
t = "bbb#extm"
expected = False
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')  



print('----------------------------')
sol = Solution()
s = "ab##"
t = "c#d#"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')  

print('----------------------------')
sol = Solution()
s = "ab#c"
t = "ad#c"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')    

print('----------------------------')
sol = Solution()
s = "a#c"
t = "b"
expected = False
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')



print('----------------------------')
sol = Solution()
s = "a##c"
t = "#a#c"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
s = "y#fo##f"
t = "y#f#o##f"
expected = True
result = sol.backspaceCompare(s,t)
print(f'result: {result}')
print(f'Is the result correct? { result == expected}')




