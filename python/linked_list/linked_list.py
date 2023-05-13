class MyNode:
    def __init__(self) -> None:
        self.value = None
        self.next = None


class MyList:
    def __init__(self, value) -> None:
        new = MyNode()
        new.value = value
        new.next = None
        
        self.head = new
        self.tail = new
        self.length = 1
        
    def append(self, value):
        new = MyNode()
        new.value = value
        new.next = self.tail
        
        self.tail = new

        self.length += 1
        
    def prepend(self, value):
        new = MyNode()
        new.value = value
        new.next = None
        
        self.head.next = new
        
        self.head = new
        
        self.length += 1
        
        
        
    def print_me(self):
        
        temp = self.tail
        while temp != None: 
            print(temp.value)
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
        
        