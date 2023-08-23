class Node:
    def __init__(self, value) -> None:
        self.left = None
        self.right = None
        self.value = value

#--------

class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_obj = Node(value)

        if self.root == None:
            self.root = new_obj
            return
        
        #---------------
        current_node = self.root
        while(True):
            if value < current_node.value: #must go to the left side
                if current_node.left == None: # found the right place - insert here
                    current_node.left = new_obj
                    return
                #----
                current_node = current_node.left #continue going to the left side
            else: #right insert
                if current_node.right == None: #found the right place - insert here
                    current_node.right = new_obj
                    return
                #----
                current_node = current_node.right
        #end of while
        #---------------


    def lookup(self):
        pass
    def remove(self):
        pass


    def print(self):
        
        node_list = []

        current = self.root
        while(current):
            left_summary = "None"
            right_summary = "None"
            if current.left:
                node_list.append(current.left)
                left_summary = current.left.value
            if current.right:
                node_list.append(current.right)
                right_summary = current.right.value

            print(f"Current value: {current.value}, current.left: {left_summary} , current.right: {right_summary}")

            current =  node_list.pop(0) if node_list else None 


#--------    

tree = BinaryTree()
tree.insert(9)
tree.print()
print(f"-------------------------------------------")
tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)
tree.print()