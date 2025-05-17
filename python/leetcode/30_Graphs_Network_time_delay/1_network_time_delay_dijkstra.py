# https://leetcode.com/problems/network-delay-time/description/


import heapq
from math import inf

import heapq
from math import inf
from typing import List, Tuple



#-------------------------------------------------------------------------
class Solution:
    # n - from 1 to 10 (the number of nodes in the system)
    # times - an array containing a list of list, the internal list is of size 3, the first number is 
    #   the source node, the second the destination node, and the third is the time cost to traverse
    # k - source signal node
    # now return the time necessary to inform all nodes. If not possible to inform all nodes return -1
    #   that means we have to traverse to all nodes, and find the shortest path to that node, and also
    #   keep track if we visited all nodes, otherwise the answer should be -1
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        time_req_list : List[int] = [inf] * n # all vertices are set to inf time, if we don't reach any of these nodes then we will know
        adj_list : List[List[int]] = [ [] for _ in range(n) ]
        
        time_req_list[k - 1] = 0 # set root vertex time to reach itself to zero
        
        #-----------------------------------
        for from_vertex, to_vertex, time_needed in times:
            adj_list[from_vertex - 1].append( ( to_vertex - 1, time_needed ) ) # from_vertex -1 -> remember we need to offset the idx
        #-----------------------------------

        heap : List[Tuple[int,int]] = [(0, k - 1)]
        #-----------------------------------
        while heap:
            current_time, current_vertex = heapq.heappop(heap)
            
            # note that all values at time_req_list start with inf, so we will look at every node at least once
            if current_time > time_req_list[current_vertex]: continue # we alread have a lower time, then skip this - but should we check its children?
            
            # then current time must be less or equal to time_req_list[current_vertex]
            time_req_list[current_vertex] = current_time
            
            #-----------------------------------
            for neigh_vertex, neigh_time_needed in adj_list[current_vertex]:
                
                new_time : int = neigh_time_needed + current_time
                
                #-----------------------------------
                if new_time < time_req_list[neigh_vertex]: #found a new shorter path
                    time_req_list[neigh_vertex] = new_time
                    
                    heapq.heappush(heap, (new_time, neigh_vertex))
                #-----------------------------------
            #-----------------------------------
        #-----------------------------------
        
        #return the answer
        max_time : int = max(time_req_list)
        
        return -1 if max_time == inf else max_time
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def networkDelayTime_old(self, times: List[List[int]], n: int, k: int) -> int:
        time_req_list : List[int] = [inf] * n # an array where each idx represent the min distance (so far) to that node
        adj_list : List[List[int]] = [[] for _ in range(n)] # an array where at idx n there's a list of all children nodes to n
        
        time_req_list[k - 1] = 0 # offset by 1 - this is our node k, the min dist/time to itself is zero

        # Use heapq (min-heap) storing tuples (distance, node_index)
        heap : List[Tuple[int,int]] = [(0, k - 1)] # the first value is node k at distance of 0
        
        ''' one important note about the algo is that we will eventually store all the nodes in
        the heap, that is all the nodes that have a connection. And we will pop the nodes with
        the smallest distance and we will check if this new node has a shorter path. If it does
        we update the shortest path.'''

        #-----------------------------------
        for from_vertex, to_vertex, time_needed in times: #create the adjacency list with times per node
            adj_list[from_vertex - 1].append((to_vertex - 1, time_needed))
        #-----------------------------------

        #-----------------------------------
        while heap:
            # Pop the node with the smallest distance
            current_time, current_vertex = heapq.heappop(heap) # pop the smallest distance/time

            ''' if current time is bigger than we already have, just ignore it. please note
            that since all edges start with 'inf' they will be put in the heap and we will
            investigate its connections at least once. '''
            if current_time > time_req_list[current_vertex]:
                continue
            
            time_req_list[current_vertex] = current_time

            #-----------------------------------
            # now let's look at the nodes connection this vertex
            for neighbour_vertex, time_needed in adj_list[current_vertex]:
                
                new_time : int = time_req_list[current_vertex] + time_needed
                
                #-----------------------------------
                if new_time < time_req_list[neighbour_vertex]: # important
                    time_req_list[neighbour_vertex] = new_time
                    
                    # Push the updated distance and neighbor to the heap
                    heapq.heappush(heap, (new_time, neighbour_vertex))
                #-----------------------------------
            #-----------------------------------
        #-----------------------------------

        max_time : int = max(time_req_list) # any node - what is the max amount to time to reach any node
        
        '''this is the part where we need to check if we reached all the nodes. The logic is
        since we started all nodes with time as 'inf' any node not reached would have
        a inf as time, and therefore the return of the maximum time should be -1.
        Otherwise, return the maximum time'''
        return -1 if max_time == inf else max_time
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
# Test case
t = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(sol.networkDelayTime(t, 5, 1))

exit()

#-------------------------------------------------------------------------
# Priority Queue implementation
class PriorityQueue:
    def __init__(self, comparator=lambda a, b: a > b):
        self._heap = []
        self._comparator = comparator

    def size(self):
        return len(self._heap)

    def peek(self):
        return self._heap[0] if self._heap else None

    def is_empty(self):
        return len(self._heap) == 0

    def _parent(self, idx):
        return (idx - 1) // 2

    def _left_child(self, idx):
        return idx * 2 + 1

    def _right_child(self, idx):
        return idx * 2 + 2

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _compare(self, i, j):
        return self._comparator(self._heap[i], self._heap[j])

    def push(self, value):
        self._heap.append(value)
        self._sift_up()
        return self.size()

    def _sift_up(self):
        node_idx = self.size() - 1
        while node_idx > 0 and self._compare(node_idx, self._parent(node_idx)):
            self._swap(node_idx, self._parent(node_idx))
            node_idx = self._parent(node_idx)

    def pop(self):
        if self.size() > 1:
            self._swap(0, self.size() - 1)
        popped_value = self._heap.pop()
        self._sift_down()
        return popped_value

    def _sift_down(self):
        node_idx = 0
        while (
            (self._left_child(node_idx) < self.size() and
             self._compare(self._left_child(node_idx), node_idx)) or
            (self._right_child(node_idx) < self.size() and
             self._compare(self._right_child(node_idx), node_idx))
        ):
            greater_child_idx = (
                self._right_child(node_idx) < self.size() and
                self._compare(self._right_child(node_idx), self._left_child(node_idx))
            )
            greater_child_idx = self._right_child(node_idx) if greater_child_idx else self._left_child(node_idx)
            self._swap(greater_child_idx, node_idx)
            node_idx = greater_child_idx
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class Solution_old:
    # n - from 1 to 10 (the number of nodes in the system)
    # times - an array containing a list of list, the internal list is of size 3, the first number is 
    #   the source node, the second the destination node, and the third is the time cost to traverse
    # k - source signal node
    # now return the time necessary to inform all nodes. If not possible to inform all nodes return -1
    #   that means we have to traverse to all nodes, and find the shortest path to that node, and also
    #   keep track if we visited all nodes, otherwise the answer should be -1
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [inf] * n # an array where each idx represent the min distance (so far) to that node
        adj_list = [[] for _ in range(n)] # an array where at idx n there's a list of all children nodes to n
        
        distances[k - 1] = 0 # offset by 1 - this is our node k, the min dist/time to itself is zero

        heap = PriorityQueue(lambda a, b: distances[a] < distances[b])
        heap.push(k - 1)

        for source, target, weight in times:
            adj_list[source - 1].append((target - 1, weight))

        while not heap.is_empty():
            current_vertex = heap.pop()

            for neighboring_vertex, weight in adj_list[current_vertex]:
                if distances[current_vertex] + weight < distances[neighboring_vertex]:
                    distances[neighboring_vertex] = distances[current_vertex] + weight
                    heap.push(neighboring_vertex)

        ans = max(distances)
        return -1 if ans == inf else ans
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
# Test case
# times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes
#  in other words: [1, 2, 9] -> from node 1 to node 2 takes 9 units of time
#  [1, 4, 2] -> from node 1 to node 4 takes 2 units of time
t = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(sol.networkDelayTime_old(t, 5, 1))