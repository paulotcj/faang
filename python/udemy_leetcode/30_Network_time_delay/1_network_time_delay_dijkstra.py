# https://leetcode.com/problems/network-delay-time/description/


import heapq
from math import inf

import heapq
from math import inf
from typing import List



#-------------------------------------------------------------------------
class Solution:
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [inf] * n
        adj_list = [[] for _ in range(n)]
        distances[k - 1] = 0

        # Use heapq (min-heap) storing tuples (distance, node_index)
        heap = [(0, k - 1)]

        for source, target, weight in times:
            adj_list[source - 1].append((target - 1, weight))

        while heap:
            # Pop the node with the smallest distance
            current_distance, current_vertex = heapq.heappop(heap)

            # If we found a shorter path already, skip
            if current_distance > distances[current_vertex]:
                continue

            for neighboring_vertex, weight in adj_list[current_vertex]:
                new_dist = distances[current_vertex] + weight
                if new_dist < distances[neighboring_vertex]:
                    distances[neighboring_vertex] = new_dist
                    # Push the updated distance and neighbor to the heap
                    heapq.heappush(heap, (new_dist, neighboring_vertex))

        ans = max(distances)
        return -1 if ans == inf else ans
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

sol = Solution()
# Test case
t = [[1, 2, 9], [1, 4, 2], [2, 5, 1], [4, 2, 4], [4, 5, 6], [3, 2, 3], [5, 3, 7], [3, 1, 5]]
print(sol.networkDelayTime(t, 5, 1))

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
    #-------------------------------------------------------------------------
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        distances = [inf] * n
        adj_list = [[] for _ in range(n)]
        distances[k - 1] = 0

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
print(sol.networkDelayTime(t, 5, 1))