#-------------------------------------------------------------------------
class MinStack:
    #-------------------------------------------------------------------------
    def __init__(self):
        self.stack_len : int = 2
        self.stack : list[int] = [None] * self.stack_len
        self.stack_pointer : int = -1
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def print_stack(self):
        print(self.stack)
    #-------------------------------------------------------------------------

    #-------------------------------------------------------------------------
    def __print_stack_stats(self):
        print('-----')
        print(f'len(self.stack) : {len(self.stack)}\tself.stack_len : {self.stack_len}\tself.stack_pointer : {self.stack_pointer}:')
        print(f'self.stack : \n{self.stack }')
        print('-----')
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __resize_stack(self , percent_stack : float = 1) -> None:
            # self.__print_stack_stats()
            #-----
            # prep the new stack - allocate memory
            new_stack_size : int = int(self.stack_len * percent_stack)
            temp_stack : list[int] = [None] * new_stack_size
            #-----
            #-----
            # copy the values over
            for idx in range(self.stack_pointer): # copy values
                temp_stack[idx] = self.stack[idx]
            #-----
            # make the new stack the actual stack
            self.stack = temp_stack
            self.stack_len = new_stack_size
            # self.__print_stack_stats()
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def push(self, val: int) -> None:
        self.stack_pointer += 1

        #---------
        if self.stack_pointer == self.stack_len : # allocate more memory
            self.__resize_stack(percent_stack=1.5)
        #---------

        self.stack[self.stack_pointer] = val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop(self) -> int:
        self.print_stack()
        if self.stack_pointer == -1 : return None
        return_val : int = self.stack[self.stack_pointer]
        self.stack[self.stack_pointer] = None

        deallocate_size_target : int = (self.stack_len * 0.75)
        if self.stack_pointer < deallocate_size_target:
            self.__resize_stack(percent_stack=0.75)        


        self.stack_pointer -= 1

        self.print_stack()

        return return_val
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def peek(self) -> int:
        if self.stack_pointer == -1 : return None
        return self.stack[self.stack_pointer]
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


stack = MinStack()
for i in range(14) :
    stack.push(i)

for i in range(14) :
    peek : int = stack.peek()
    pop : int = stack.pop()
    print(f'------- pop  : {pop}')
    print(f'------- peek : {peek}')
    print(f'------- peek == pop : {peek==pop}')
