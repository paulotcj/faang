# https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list


from typing import Optional, List
#-------------------------------------------------------------------------
class Node:
    #-------------------------------------------------------------------------
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class ProcessList:
    #-------------------------------------------------------------------------
    def create_from_array( arr : List[int] ) -> Node :
        nodes_list : List[Node] = []
        
        # create the list
        #-----------------------------------
        for loop_idx, loop_val in enumerate(arr) :
            if loop_val :
                temp : Node = Node(val = loop_val, prev = None , next = None, child = None)
                nodes_list.append(temp)
            else:
                nodes_list.append(None)
        #-----------------------------------
        
        prev : Node = None
        curr : Node = None
        next : Node = None
        
        #adjust next and prev pointers
        #-----------------------------------
        for loop_idx, loop_val in enumerate(nodes_list) :
            # this means this level has ended and we are about to start a new sublevel list, 
            #  so we reset all pointers
            #--------
            if loop_val is None : 
                prev = None
                curr = None
                next = None
                continue
            #--------
            
            curr = loop_val
            curr.prev = prev
            if prev is not None: prev.next = curr
            
            prev = curr # adjust the pointer before the next loop
        #-----------------------------------
        
        parent_list_start, i = 0, 0
        #-----------------------------------
        while i < len(nodes_list):
            #-----------------------------------
            if nodes_list[i] is None : # this first none indicates a new sublist has started
                sublist_offset : int = -1 # assumes -1 since the first None will count +1 and it will be position 0
                
                # position the sublist_offset
                #-----------------------------------
                while nodes_list[i] is None and i < len(nodes_list):
                    sublist_offset += 1
                    i += 1
                #-----------------------------------
                
                # now parent_list_start is pointing at the index where this list starts
                #  sublist_offset tells how many steps we need to skip to find the parent
                #  node of this new sublist
                
                nodes_list[ parent_list_start + sublist_offset ].child = nodes_list[i]
                
                # now this is a potential start for a new sublist, so we keep track of it
                parent_list_start = i                
            #-----------------------------------
            i += 1 # loop
        #-----------------------------------
        
        # now what to return? nodes_list[0]
        return_obj : Node = nodes_list[0] if nodes_list else None
        return return_obj
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def print_linked_list(head : Node) -> List[int] :
        curr : Node = head
        list : List[int] = []
        #-----------------------------------
        while curr is not None:
            list.append(curr.val)
            curr = curr.next
        #-----------------------------------
        
        print(list)
        return list
        
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def flatten( self , head : 'Optional[Node]' ) -> 'Optional[Node]' :
        curr : Node = head
        list_node : List[Node] = []
        stack_pending_nodes : List[Node] = []
        
        #-----------------------------------
        while curr:
            list_node.append(curr)
            
            #-------
            if curr.child: #if the node has a child start processing the child's list
                stack_pending_nodes.append(curr) # stack saving point from where the operation will resume from
                curr = curr.child # take the fork path
                # at this point loop with current being a valid node, so none of the logic 
                #  below applies
                continue
            #-------
                
            curr = curr.next
            # might've reached the end of this list, now it's necessary to check if the stack
            #  has any elements on it, if so, resume processing from there
            while curr is None and stack_pending_nodes:
                curr = stack_pending_nodes.pop().next
        #-----------------------------------
        
        #-----------------------------------
        for loop_idx, loop_val in enumerate(list_node):
            
            # fix prev - note: skip fix prev for the first node
            if loop_idx > 0 : 
                list_node[loop_idx].prev = list_node[loop_idx - 1]
                
            # fix next - skip the last one
            if loop_idx < len(list_node) - 1 :
                list_node[loop_idx].next = list_node[loop_idx + 1]
                
            # don't know if this is necessary
            loop_val.child = None
        #-----------------------------------
        
        return head # head will always be the head
        
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------


print('----------------------------')
sol = Solution()
arr = [1,2,3,4,5,6,None,None,None,7,8,None,None,11,12]
# 1,2,3,4,5,6
#     7,8
#       11,12
expected = [1,2,3,7,8,11,12,4,5,6]
# error generated: [1,2,3,7,8,11,12]
head = ProcessList.create_from_array(arr = arr)


head = sol.flatten(head)
result = ProcessList.print_linked_list(head)
print(f'result  : {result}')
print(f'expected: {expected}')
print(f'Is the result correct? { result == expected}')


print('----------------------------')
sol = Solution()
arr = [ 1, 2, 3, 4, 5, 6, None, None, None, 7, 8, 9, 10, None, None, 11, 12 ]

expected = [1,2,3,7,8,11,12,9,10,4,5,6]
head = ProcessList.create_from_array(arr = arr)


head = sol.flatten(head)
result = ProcessList.print_linked_list(head)
print(f'result  : {result}')
print(f'expected: {expected}')
print(f'Is the result correct? { result == expected}')
# exit()


