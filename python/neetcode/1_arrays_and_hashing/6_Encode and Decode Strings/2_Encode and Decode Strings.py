#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def encode(self, strs: list[str]) -> str:

        temp_list : list[str] = [ 
            f"{str(len(loop_str))}#{loop_str}" 
            for loop_str in strs 
        ]
        return_obj : str = ''.join(temp_list)
        return return_obj
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def decode(self, s: str) -> list[str]:
        
        return_obj : list[str] = []
        #--------------------------------------------------
        while "#" in s:
            str_len , s = s.split("#",1)
            end : int = int(str_len)

            temp_str = s[: end]
            return_obj.append(temp_str)
            s = s[end:]
        #--------------------------------------------------

        return return_obj
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
        


print('------------------------------------')
sol = Solution()

input = ["neet","code","love","you"]
expected = "4#neet4#code4#love3#you"
result = sol.encode(strs=input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

#-----
input = "4#neet4#code4#love3#you"
expected = ["neet","code","love","you"]
result = sol.decode(s=input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
sol = Solution()

input = ["we","say",":","yes"]
expected = "2#we3#say1#:3#yes"
result = sol.encode(strs=input)
print(result)


is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

#-----
input = "2#we3#say1#:3#yes"
expected = ["we","say",":","yes"]
result = sol.decode(s = input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



