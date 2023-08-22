class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class Qeue:
    def __init__(self)-> None:
        self.first = None
        self.last = None
        self.len = 0

    def peek(self):
        return self.first
    
    def enqueue(self, value):
        new_entry = Node(value)
        if self.first == None: #that means the queue is empty
            self.first = new_entry
            self.last = new_entry
        else:
            self.last.next = new_entry
            self.last = new_entry

        self.len += 1


    def dequeue(self):
        if self.len == 0: return None

        return_obj = self.first
        self.first = self.first.next
        return_obj.next = None #erase the reference

        self.len -= 1

        return return_obj
        

#------------------------------------------        
# peek.value if peek != None else ''

my_queue = Qeue()

dequeue = my_queue.dequeue() #test dequeue in a empty array
peek = my_queue.peek()
print(f"peek: { peek.value if peek != None else '' } - Queue Len: {my_queue.len}")
my_queue.enqueue('test1')


peek = my_queue.peek()
print(f"peek: {peek.value if peek != None else '' } - Queue Len: {my_queue.len}")
my_queue.enqueue('test2')
peek = my_queue.peek()
print(f"peek: {peek.value if peek != None else '' } - Queue Len: {my_queue.len}")
my_queue.enqueue('test3')
peek = my_queue.peek()
print(f"peek: {peek.value if peek != None else '' } - Queue Len: {my_queue.len}")


print(f"---------------------")
peek = my_queue.peek()
print(f"peek: {peek.value if peek != None else '' } - Queue Len: {my_queue.len}")
dequeue = my_queue.dequeue()
print(f"dequeue: {dequeue.value if peek != None else '' } - Queue Len: {my_queue.len}")

print(f"---------------------")
peek = my_queue.peek()
print(f"peek: {peek.value if peek != None else '' } - Queue Len: {my_queue.len}")
dequeue = my_queue.dequeue()
print(f"dequeue: {dequeue.value if peek != None else '' } - Queue Len: {my_queue.len}")


print(f"---------------------")
peek = my_queue.peek()
print(f"peek: {peek.value if peek != None else '' } - Queue Len: {my_queue.len}")
dequeue = my_queue.dequeue()
print(f"dequeue: {dequeue.value if peek != None else '' } - Queue Len: {my_queue.len}")

print(f"---------------------")
peek = my_queue.peek()
print(f"peek: {peek.value if peek != None else '' } - Queue Len: {my_queue.len}")
dequeue = my_queue.dequeue()
print(f"dequeue: {dequeue.value if peek != None else '' } - Queue Len: {my_queue.len}")
