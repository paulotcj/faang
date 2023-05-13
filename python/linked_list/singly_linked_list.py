class MyNode:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class MyList:
    def __init__(self, value) -> None:
        new = MyNode(value)
        
        self.head = new
        self.tail = new
        self.length = 1
        
    def append(self, value):
        new = MyNode(value)

        new.next = self.tail #for this new node the 'next node' is the current tail
        
        self.tail = new #the 'tail' pointer in this linked list will point to the new node

        self.length += 1
        
    def prepend(self, value):
        new = MyNode(value)

        #the self.head.next tipically point to None, since there's nothing else after or above the head
        # so we temporarily make the self.head.next to point to the new node
        self.head.next = new 
        
        #and now we make the linked list pointer self.head to point to new, and considering the new node has
        #  new.next equals to None, no further action is necessary
        self.head = new 
        
        self.length += 1
        
        
        
    def print_me(self):
        
        temp = self.tail
        while temp != None: 
            print(f"{temp.value}{ ' -> tail' if temp == self.tail else '' }{ ' -> head' if temp == self.head else '' }")
            temp = temp.next
            
        print("----------------")
        
        # print(f"head: {self.head.next} - tail: {self.tail.next} - len:{self.length}")    
    
    
    
x = MyList(10)
x.print_me()
x.append(11)
x.print_me()

x.append(22)
x.append(33)
x.append(44)
x.append(55)
x.append(66)
x.append(77)
x.print_me()
x.append(88)
x.print_me()

x.prepend(111)
x.print_me()
        
        