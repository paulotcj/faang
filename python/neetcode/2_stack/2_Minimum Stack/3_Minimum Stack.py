#-------------------------------------------------------------------------
class MinStack:
    #-------------------------------------------------------------------------
    def __init__(self):
        self.stack : list[int] = []
        self.min : int = None

    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def push(self, val: int) -> None:

        if not self.stack:
            self.stack.append(0)
            self.min = val
        else:
            new_temp_val : int = val - self.min
            self.stack.append(new_temp_val)
            if val < self.min:
                self.min = val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop(self) -> int:
        if not self.stack : return None


        pop : int = self.stack.pop()

        if pop < 0:
            self.min = self.min - pop

        return_pop_val : int = self.min + pop
        return return_pop_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def top(self) -> int:
        if not self.stack : return None
        top_val : int = self.stack[-1]
        if top_val > 0 : return top_val + self.min
        else: return self.min
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def getMin(self) -> int:
        return self.min
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

# minStack = MinStack()
# minStack.push(-99)
# minStack.push(-9)
# minStack.push(-100)
# print(minStack.pop())
# print(minStack.pop())
# exit()


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
