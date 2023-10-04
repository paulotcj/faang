



class BinaryTreeArray:
    def __init__(self):
        self.tree = []
        self.count = 0
        self.level = 0
        self.capacity = 0

        def add_capacity(self):
            self.capacity = 2 ** self.level + self.capacity
            self.level += 1

            loop_range = self.capacity - self.count
            for _ in range(loop_range):
                self.tree.append(None)


        def insert(self, value):
            if self.count + 1 > self.capacity: self.add_capacity()

            self.count +=1 
