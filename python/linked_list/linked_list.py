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

        new.next = self.tail
        
        self.tail = new

        self.length += 1
        
    def prepend(self, value):
        new = MyNode(value)

        
        self.head.next = new
        
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
        
        