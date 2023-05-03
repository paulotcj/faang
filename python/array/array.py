class MyArray:
    def __init__(self):
        self.length = 0
        self.data = []
        
    def get(self,index):
        return self.data[index]
    
    def push(self, element):
        # self.data.append(element) #you could do this, but this is not the spirit of this exercise
        self.data.insert(self.length, element)
        self.length += 1
        return self.data
    
    def pop(self):
        # self.data.pop() # you could do this
        last_item = self.data.pop(self.length-1)
        self.length -= 1
        return last_item
    
    def deleteAtIndex(self, index):
        # item = self.data.pop(index)
        # self.length -+ 1
        item = self.data[index]
        self.shiftItems(index)
        return item
    
    def shiftItems(self,index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
            
        self.data.pop()
        self.length -= 1
            
    
    
x = MyArray()
print(f"x.length : {x.length} , x.data: {x.data}")
x.push('hi')
x.push('you')
x.push('!')
print(f"x.length : {x.length} , x.data: {x.data}")


print(f"x.get(1) : {x.get(1)}")
# print(x.data[0])
# print(x.data[1])
# print(x.data[2])

print(f"x.pop() : {x.pop()}")
print(f"x.length : {x.length} , x.data: {x.data}")

print(f"x.deleteAtIndex(0) {x.deleteAtIndex(0)} ")

x.push("are")
x.push("nice")

print(f"x.length : {x.length} , x.data: {x.data}")

