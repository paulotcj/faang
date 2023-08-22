



class Stack:
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        return self.top
    
    def push(self,value):
        new_node = Node(value)
        if(self.length == 0):
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.length += 1
        

    def pop(self):
        if(self.top == None):
            return None
        if(self.top == self.bottom): #If theres only one element, we set the bottom as None for now and that's
            self.bottom = None       # because in this case the top will also be set to none eventually
        #---
        #shifting things
        temp = self.top
        self.top = self.top.next #this might be None
        self.length -= 1
        #---
        temp.next = None #we need to eliminate previous references
        return temp


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

#------------------------------------------

my_stack = Stack()

peek = my_stack.peek()
print(f"peek: { peek.value if peek != None else '' } - Stack Len: {my_stack.length}")
my_stack.push('test1')
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.length}")
my_stack.push('test2')
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.length}")
my_stack.push('test3')
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.length}")

print(f"---------------------")
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.length}")
pop = my_stack.pop()
print(f"pop: {pop.value if peek != None else '' } - Stack Len: {my_stack.length}")

print(f"---------------------")
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.length}")
pop = my_stack.pop()
print(f"pop: {pop.value if peek != None else '' } - Stack Len: {my_stack.length}")


print(f"---------------------")
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.length}")
pop = my_stack.pop()
print(f"pop: {pop.value if peek != None else '' } - Stack Len: {my_stack.length}")

print(f"---------------------")
peek = my_stack.peek()
print(f"peek: {peek.value if peek != None else '' } - Stack Len: {my_stack.length}")
pop = my_stack.pop()
print(f"pop: {pop.value if peek != None else '' } - Stack Len: {my_stack.length}")



# print(f"")
