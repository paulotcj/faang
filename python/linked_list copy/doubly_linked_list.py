
class MyNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class MyList:
    def __init__(self, value):
        new = MyNode(value = value)
        self.head = new
        self.tail = new
        self.len = 1
        
    def append(self, value):
        new = MyNode(value = value)
        
        new.next = self.tail
        
        self.tail.prev = new
        self.tail = new
        
        self.len += 1
        
    def print_me(self):
        
        idx = self.len - 1
        temp = self.tail
        while temp != None: 
            print(f"[{idx}] - v : {temp.value}{ ' -> tail' if temp == self.tail else '' }{ ' -> head' if temp == self.head else '' }")
            idx -= 1
            temp = temp.next
            
        print("----------------")
        
    def prepend(self, value):
        new = MyNode(value=value)
        
        new.prev = self.head
        self.head.next = new
        
        self.head = new
        self.len += 1
        
        
    def traverse_to_idx(self, index):
        if index <= 0 : return self.head
        elif index > (self.len - 1): return self.tail
        
        loops = index

        temp_node = self.head
        while loops > 0:
            temp_node = temp_node.prev
            loops -= 1
            
        return temp_node
    
    def insert_at(self,index, value):
        
        if self.len <= 0:
            new_node = MyNode(value)
            self.head = new_node
            self.tail = new_node
            self.len = 1
            return
        
        if index <= 0: 
            self.prepend(value)
            return
        elif index >= self.len: 
            self.append(value)
            return
        
        new = MyNode(value)

        node_at_index = self.traverse_to_idx(index)
        
        node_at_index.next.prev = new
        
        new.prev = node_at_index
        new.next = node_at_index.next
        
        node_at_index.next = new
        
        self.len += 1
        
    def remove_at(self,index):
        #fixing out of bounds index
        if index < 0 : index = 0
        elif index >= self.len: index = self.len - 1
        
        if self.len <= 0: 
            return
        elif self.len <= 1:
            self.head = None
            self.tail = None
            self.len = 0
            return
        
        if index == 0:            
            self.head = self.head.prev
            self.head.next = None
        elif index == (self.len-1):
            self.tail = self.tail.next
            self.tail.prev = None
        else:
            remove = self.traverse_to_idx(index=index)
            
            remove.next.prev = remove.prev
            remove.prev.next = remove.next
        
        self.len -= 1

        
        

        
        

            
            
        
        

        
        
x = MyList(10)
x.print_me()
x.append(11)
x.print_me()
x.append(22)
x.append(33)
x.print_me()
x.prepend(12)
x.print_me()
 
 
y = 3
print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")
y = 0
print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")
y = -1
print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")
y = 9
print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")
y = 4
print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")
        
        
x.insert_at(index = 2, value = 2)
x.print_me()
x.insert_at(index = 2, value = 4)
x.print_me()
x.insert_at(index = 2, value = 5)
x.print_me()
x.insert_at(index = 4, value = 44)
x.print_me()
x.insert_at(index = -1, value = 6)
x.print_me()
x.insert_at(index = 0, value = 7)
x.print_me()
x.insert_at(index = 22, value = 8)
x.print_me()
x.insert_at(index =11, value = 9)
x.print_me()

x = MyList(10)
# x.append(11)
x.print_me()
x.remove_at(0)
x.print_me()
x.remove_at(0)
x.print_me()

x = MyList(10)
x.append(11)
x.print_me()
x.remove_at(0)
x.print_me()

x = MyList(10)
x.append(11)
x.print_me()
x.remove_at(1)
x.print_me()
x.remove_at(1)
x.print_me()
#----------------
x = MyList(10)
x.append(11)
x.append(22)
x.append(33)
x.append(44)
x.append(55)
x.print_me()
x.remove_at(-1)
x.print_me()
x.remove_at(0)
x.print_me()



x = MyList(10)
x.append(11)
x.append(22)
x.append(33)
x.append(44)
x.append(55)
x.print_me()
x.remove_at(6)
x.print_me()
x.remove_at(4)
x.print_me()

x = MyList(10)
x.append(11)
x.append(22)
x.append(33)
x.append(44)
x.append(55)
x.print_me()
x.remove_at(3)
x.print_me()
