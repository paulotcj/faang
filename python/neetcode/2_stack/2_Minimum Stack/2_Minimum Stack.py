#-------------------------------------------------------------------------
class MinStack:
    #-------------------------------------------------------------------------
    def __init__(self):
        self.stack : list[int] = []
        self.aux_stack : list[int] = []
        self.min : int = None
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min = min(self.min , val)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop(self) -> int:
        return self.stack.pop()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def top(self) -> int:
        return self.stack[-1]
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def getMin(self) -> int:

    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('------------------------------------')


minStack = MinStack()
minStack.push(1)
minStack.push(2)
minStack.push(0)

result = minStack.getMin() # return 0
expected = 0
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')



minStack.pop()
result =  minStack.top()    # return 2
expected = 2
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')


result = minStack.getMin() # return 1
expected = 1
is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')




is_equal = expected == result
if is_equal:
    status_result = f"\033[1;97;42m{is_equal}\033[0m"  # Bold, white text, green background
else:
    status_result = f"\033[1;97;41m{is_equal}\033[0m"  # Bold, white text, red background
print(f'is the result what was expected? {status_result} - expected: {expected} - result : {result}')
