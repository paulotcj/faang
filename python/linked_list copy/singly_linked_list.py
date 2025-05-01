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
        
        idx = self.length - 1
        temp = self.tail
        while temp != None: 
            print(f"[{idx}] - v : {temp.value}{ ' -> tail' if temp == self.tail else '' }{ ' -> head' if temp == self.head else '' }")
            idx -= 1
            temp = temp.next
            
        print("----------------")
        
        # print(f"head: {self.head.next} - tail: {self.tail.next} - len:{self.length}")   
        
    def traverse_to_idx(self, index):
        loops = (self.length - index) - 1
        if loops < 0: return None
        
        temp_node = self.tail
        while temp_node != None and loops > 0:
            temp_node = temp_node.next
            loops -= 1
            
        return temp_node
    
    def insert_at(self,index,value):
        
        if self.length <= 0: #can you insert at an empty list?
            new = MyNode(value)
            self.head = new
            self.tail = new
            self.length = 1
            return
            
        elif index > (self.length-1):
            self.append(value)
            return
        elif index <= 0:
            self.prepend(value)
            return
            
        new = MyNode(value)
        node_at_index = self.traverse_to_idx(index=index)
        
        new.next = node_at_index.next
        
        node_at_index.next = new
        
        self.length += 1
        
    def remove_at(self,index):
        
        if index > self.length-1: index = (self.length-1)
        elif index < 0: index = 0
        
        if self.length <= 1: #list has a len of 1 or 0 and now becomes an empty list
            self.head = None
            self.tail = None
            self.length = 0
            return
        
        elif index >= (self.length-1): #removing at the len
            self.tail = self.tail.next
            self.length -= 1
            return

        #we guarantee now that we have at least 3 elements in our list
        # because if we had one it would be caught in the first if
        # if we had 2 we would remove from tail
        
        #(index+1) because we want to stop at the node before the one being removed
        node = self.traverse_to_idx(index= (index+1))
        
        node.next = node.next.next
        self.length -= 1
        
        
        
        
        
             
    
#------------------------------------------
#------------------------------------------
#------------------------------------------
#--------
#-------- TESTS
#--------
#------------------------------------------
#------------------------------------------
#------------------------------------------  
    
x = MyList(10)
x.print_me()
x.append(11)
x.print_me()
#------------
x = MyList(10)
x.print_me()
x.append(11)
x.append(22)
x.append(33)
x.print_me()
x.prepend(9)
x.print_me()






y = 3
print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")
y = 0
print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")
# y = -1
# print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")

y = 4
print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}")
# y = 5
# print(f"x.traverse_to_idx({y}).value : {x.traverse_to_idx(y).value}") #error


x.insert_at(index= -1 , value = 2)
x.print_me()

x.insert_at(index= 0 , value = 3)
x.print_me()

x.insert_at(index= 4 , value = 5)
x.print_me()

x.insert_at(index= 100 , value = 7)
x.print_me()

x.insert_at(index= 8 , value = 13)
x.print_me()



x.remove_at(15)
x.print_me()


x.remove_at(99)
x.print_me()

x.remove_at(7)
x.print_me()

x.remove_at(4)
x.print_me()

x.remove_at(-1)
x.print_me()

x.remove_at(0)
x.print_me()


x = MyList(10)
x.remove_at(99)
x.print_me()


x = MyList(10)
x.append(11)
x.print_me()
x.remove_at(99)
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

x = MyList(10)
x.append(11)
x.print_me()
x.remove_at(2)
x.print_me()




x = MyList(10)
x.append(11)
x.append(22)
x.print_me()
x.remove_at(-1)
x.print_me()


x = MyList(10)
x.append(11)
x.append(22)
x.print_me()
x.remove_at(0)
x.print_me()


x = MyList(10)
x.append(11)
x.append(22)
x.print_me()
x.remove_at(1)
x.print_me()

x = MyList(10)
x.append(11)
x.append(22)
x.print_me()
x.remove_at(2)
x.print_me()


x = MyList(10)
x.append(11)
x.append(22)
x.print_me()
x.remove_at(3)
x.print_me()


x = MyList(10)
x.print_me()
x.remove_at(3)
x.remove_at(3)
x.print_me()
        
        