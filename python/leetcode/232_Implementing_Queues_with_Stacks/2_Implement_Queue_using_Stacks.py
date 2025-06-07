#problem: https://leetcode.com/problems/implement-queue-using-stacks/description/
from typing import List, Dict

#-------------------------------------------------------------------------
class MyQueue :
    #-------------------------------------------------------------------------
    def __init__( self ) :
        self.stack1 : list[int] = []
        self.stack2 : list[int] = []
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def empty( self ) -> bool :
        return_result : bool = not ( self.stack1 or self.stack2 )
        return return_result
    #------------------------------------------------------------------------- 
    #-------------------------------------------------------------------------
    def push( self , x : int ) -> None :
        self.stack1.append(x)
    #-------------------------------------------------------------------------
    ''' up until now it wasn't necessary to worry about stacks or queues. but the methods
    below will take that into consideration. A queue is FIFO - first in first out. And if
    a list were to be used, although python do provide methods for poping elements at idx 0
    we would be violating the problem guidelines. So the solution then is:
     Pushing numbers to stack1: [1,2,3,4,5,6]
     Using the logic of a queue, we would expect the output to be: [1,2,3,4,5,6]
     but we can only use the method pop as the problem's constraints, therefore the result
     would be: [6,5,4,3,2,1]
     To solve this issue, we use a second stack 'stack2' where we push the output of stack1:
       [6,5,4,3,2,1] and then we get [1,2,3,4,5,6] '''

    #-------------------------------------------------------------------------
    def __transfer(self):
        #-----------------------------------
        while self.stack1:
            popped : int = self.stack1.pop()
            self.stack2.append(popped) 
        #-----------------------------------
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def peek( self ) -> int:
        #-----
        if self.stack2: 
            return self.stack2[-1] # if there's already elements at stack2, just return it
        #-----
        if self.stack1 : # no elements at stack2
            self.__transfer() # try to transfer some elements from stack1 to stack2
            #-----
            if self.stack2: return self.stack2[-1]
            #-----
        #-----
            
        return None # this should not happen as per problem's constraints
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def pop( self ) -> int :
        if self.stack2: return self.stack2.pop() # if there's already elements at stack2, just return it
        
        if self.stack1:
            self.__transfer() # try to transfer some elements from stack1 to stack2
            if self.stack2 : return self.stack2.pop()
            
        return None # this should not happen as per problem's constraints
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

