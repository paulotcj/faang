#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def encode(self, strs: list[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def decode(self, s: str) -> list[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j

        return res
        #--------------------------------------------------

        #--------------------------------------------------


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
        


print('------------------------------------')
sol = Solution()

input = ["neet","code","love","you"]
expected = "4,4,4,3#neetcodeloveyou"
result = sol.encode(strs=input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

#-----
input = "4,4,4,3#neetcodeloveyou"
expected = ["neet","code","love","you"]
result = sol.decode(s = input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



print('------------------------------------')
sol = Solution()

input = ["we","say",":","yes"]
expected = "2,3,1,3#wesay:yes"
result = sol.encode(strs=input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')

#-----
input = "2,3,1,3#wesay:yes"
expected = ["we","say",":","yes"]
result = sol.decode(s = input)

is_equal = expected == result
if is_equal:
    status_result = f"\033[1;37;42m{expected == result}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;37;41m{expected == result}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



