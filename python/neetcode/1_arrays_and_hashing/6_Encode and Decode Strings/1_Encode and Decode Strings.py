#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def encode(self, strs: list[str]) -> str:
        if not strs : return ""

        sizes : list[str] = [ str(len(loop_str)) for loop_str in strs ]

        return_obj : str = f"{ ','.join(sizes) }#{ ''.join(strs) }"

        return return_obj
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def decode(self, s: str) -> list[str]:
        if not s: return []

        sizes , strings_pack = s.split("#",1)
        sizes : list[int] = [ int(size) for size in sizes.split(",")]
        
        return_obj : list[str] = []
        start : int = 0
        #--------------------------------------------------
        for str_len in sizes:
            end : int = start + str_len
            temp_str : str = strings_pack[start:end]
            return_obj.append( temp_str )
            start = end
        #--------------------------------------------------

        return return_obj
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
        


print('------------------------------------')
sol = Solution()

input = ["neet","code","love","you"]
expected = "4,4,4,3#neetcodeloveyou"
result = sol.encode(strs=input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

#-----
input = "4,4,4,3#neetcodeloveyou"
expected = ["neet","code","love","you"]
result = sol.decode(s = input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
sol = Solution()

input = ["we","say",":","yes"]
expected = "2,3,1,3#wesay:yes"
result = sol.encode(strs=input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

#-----
input = "2,3,1,3#wesay:yes"
expected = ["we","say",":","yes"]
result = sol.decode(s = input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



