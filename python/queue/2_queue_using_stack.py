# class Node:
#     def __init__(self,value) -> None:
#         self.value = value
#         self.next = None

      
class MyQueue:

    def __init__(self):
        self.array = []

    def len(self):
        return len(self.array)
        

    def push(self, x: int) -> None:
        self.array.append(x)
        

    def pop(self) -> int:
        if self.len() == 0: return None

        # return_obj = self.array[0]
        return_obj = self.array.pop(0)
        return return_obj
        

    def peek(self) -> int:
        if self.len() == 0: return None

        return self.array[0]
        

    def empty(self) -> bool:
        return True if self.len()==0 else False

#------------------------------------------        


#------------------------------------------        
# peek.value if peek != None else ''

my_queue = MyQueue()

dequeue = my_queue.pop() #test dequeue in a empty array
peek = my_queue.peek()
print(f"peek: { peek if peek != None else '' } - Queue Len: {my_queue.len()}")
my_queue.push(1)


peek = my_queue.peek()
print(f"peek: {peek if peek != None else '' } - Queue Len: {my_queue.len()}")
my_queue.push(2)
peek = my_queue.peek()
print(f"peek: {peek if peek != None else '' } - Queue Len: {my_queue.len()}")
my_queue.push(3)
peek = my_queue.peek()
print(f"peek: {peek if peek != None else '' } - Queue Len: {my_queue.len()}")


print(f"---------------------")
peek = my_queue.peek()
print(f"peek: {peek if peek != None else '' } - Queue Len: {my_queue.len()}")
dequeue = my_queue.pop()
print(f"dequeue: {dequeue if peek != None else '' } - Queue Len: {my_queue.len()}")

print(f"---------------------")
peek = my_queue.peek()
print(f"peek: {peek if peek != None else '' } - Queue Len: {my_queue.len()}")
dequeue = my_queue.pop()
print(f"dequeue: {dequeue if peek != None else '' } - Queue Len: {my_queue.len()}")


print(f"---------------------")
peek = my_queue.peek()
print(f"peek: {peek if peek != None else '' } - Queue Len: {my_queue.len()}")
dequeue = my_queue.pop()
print(f"dequeue: {dequeue if peek != None else '' } - Queue Len: {my_queue.len()}")

print(f"---------------------")
peek = my_queue.peek()
print(f"peek: {peek if peek != None else '' } - Queue Len: {my_queue.len()}")
dequeue = my_queue.pop()
print(f"dequeue: {dequeue if peek != None else '' } - Queue Len: {my_queue.len()}")
