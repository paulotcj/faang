import heapq
import math

class A_Star_Pathfinding:
    def __init__(self, graph, element_locations):
        self.graph = graph
        self.element_locations = element_locations

    def heuristic(self, a, b):
        (x1, y1) = self.element_locations[a]
        (x2, y2) = self.element_locations[b]
        return abs(x1 - x2) + abs(y1 - y2)

    def add_edge(self, from_node, to_node):
        if from_node not in self.graph:
            self.graph[from_node] = {}
        self.graph[from_node][to_node] = self.heuristic(from_node, to_node)

    def a_star_search(self, start, goal):
        frontier = []
        heapq.heappush(frontier, (0, start))
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while frontier:
            (priority, current) = heapq.heappop(frontier)

            if current == goal:
                break

            for next_node in self.graph[current]:
                new_cost = cost_so_far[current] + self.graph[current][next_node]
                if next_node not in cost_so_far or new_cost < cost_so_far[next_node]:
                    cost_so_far[next_node] = new_cost
                    priority = new_cost + self.heuristic(goal, next_node)
                    heapq.heappush(frontier, (priority, next_node))
                    came_from[next_node] = current

        return came_from, cost_so_far