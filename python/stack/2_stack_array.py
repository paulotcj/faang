class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None


class Stack:
    def __init__(self)->None:
        self.array = []

    def len(self):
        return len(self.array)

    def peek(self):
        if self.array: 
            return self.array[-1]
        else: 
            return None

    def pop(self):
        if self.array:
            return self.array.pop()
        else:
            return None

    def push(self, value):
        new_element = Node(value)
        self.array.append(new_element)
        



#------------------------------------------        


my_stack = Stack()

my_stack.pop() #test pop in a empty array

peek = my_stack.peek()
print(f"peek: { peek.value if peek != None else '' } - Stack Len: {my_stack.len()}")
my_stack.push('test1')
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.len()}")
my_stack.push('test2')
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.len()}")
my_stack.push('test3')
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.len()}")

print(f"---------------------")
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.len()}")
pop = my_stack.pop()
print(f"pop: {pop.value if peek != None else '' } - Stack Len: {my_stack.len()}")

print(f"---------------------")
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.len()}")
pop = my_stack.pop()
print(f"pop: {pop.value if peek != None else '' } - Stack Len: {my_stack.len()}")


print(f"---------------------")
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.len()}")
pop = my_stack.pop()
print(f"pop: {pop.value if peek != None else '' } - Stack Len: {my_stack.len()}")

print(f"---------------------")
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.len()}")
pop = my_stack.pop()
print(f"pop: {pop.value if peek != None else '' } - Stack Len: {my_stack.len()}")
