import heapq
import math


#-------------------------------------------------------------------------
class A_Star_Pathfinding:
    #-------------------------------------------------------------------------
    def __init__(self, graph, element_locations):
        self.graph = graph
        self.element_locations = element_locations
        self.heuristic_distances = {}
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __calc_distance(self, node1, node2):
        dist1 = node2[0] - node1[0]
        dist2 = node2[1] - node1[1]
        dist = math.sqrt(dist1**2 + dist2**2)
        return dist
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def add_edge(self,node1, node2):
        #graph_dict is a dictionary of dictionaries
        if node1 not in self.graph:
            self.graph[node1] = {}
        if node2 not in self.graph:
            self.graph[node2] = {}

        distance = self.__calc_distance(self.element_locations[node1], self.element_locations[node2])

        # self.graph[node1][node2] = {'edge': distance, 'heuristic': float('infinity')}
        # self.graph[node2][node1] = {'edge': distance, 'heuristic': float('infinity')}
        self.graph[node1][node2] = distance
        self.graph[node2][node1] = distance
        # print(graph_dict)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __find_heuristic(self, end):
        node2 = self.element_locations[end]
        for e in self.graph:
            node1 = self.element_locations[e]
            distance = self.__calc_distance(node1, node2)
            self.heuristic_distances[e] = distance
            


    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dijkstra(self, start, end):
        #modified Dijkstra's algorithm to use A* pathfinding
        graph = self.graph
        #--------------------
        self.__find_heuristic(end)
        #--------------------
        # prep:   heuristic                        dist  node
        queue = [(self.heuristic_distances[start], 0,    start)]

        distances = {node: [float('infinity'), self.heuristic_distances[node], float('infinity')] 
                     for node in graph} # creates a dictionary, the keys are the nodes in the graph, and the values are initially set to 'infinity'
        distances[start][0] = 0 
        path_table = {node: None for node in graph}
        #--------------------
        while queue:
            heuristic, inspecting_node_distance, inspecting_node = heapq.heappop(queue)
            #-----
            saved_distance = distances[inspecting_node][0]
            if inspecting_node_distance <= saved_distance: # even if its the same distance, we still want to process it, because we might find a shorter path down the road
                self.calculate_new_distance(graph = graph, queue = queue, distances = distances,
                                    path_table = path_table, inspecting_node = inspecting_node,
                                    inspecting_node_distance = inspecting_node_distance,
                                    end_node = end)
                
                if distances[end][0] < float('infinity'): #found a path
                    break
            #-----
        #end of while
        #--------------------
        return distances, path_table
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def calculate_new_distance(self, graph, queue, distances, path_table, inspecting_node, inspecting_node_distance, end_node):
        # the current distance is calculated from the perspective of the start node
        connections_to_curr_node = graph[inspecting_node]
        for neighbor, neighbor_distance in connections_to_curr_node.items(): #from the perspective of the current node, we connect the current shortest distance of this node to its neighbors, and check if we found a new shorter path
            
            new_distance = inspecting_node_distance + neighbor_distance #new distance to the neighbor, perhapes we found a new shorter path?

            if new_distance < distances[neighbor][0]:
                distances[neighbor][0] = new_distance
                distances[neighbor][2] = new_distance + self.heuristic_distances[neighbor]
                path_table[neighbor] = inspecting_node
                temp = self.heuristic_distances[neighbor] + new_distance
                heapq.heappush(queue, (temp, new_distance, neighbor))

                if neighbor == end_node: 
                    print('hi')
                    return
                
       
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def shortest_path(self, start, end):
        distances, previous_nodes = self.dijkstra(start,end)
        path = []
        while end is not None:
            path.append([end, distances[end][0]])
            end = previous_nodes[end]
        return path[::-1]               
    #-------------------------------------------------------------------------


#-------------------------------------------------------------------------

graph = {}
element_locations = { 'A': [1,1], 'B': [1,7] , 'C' : [7,7] }


x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)
x.add_edge("A", "B")
x.add_edge("A", "C")
x.add_edge("B", "C")

print(x.shortest_path("A", "C"))

# print('----------------------------------')

# graph = {}
# element_locations = { 'A': [1,1], 'B': [1,7] , 'C' : [7,7], 'D': [1,8] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

# x.add_edge("A", "D")
# x.add_edge("A", "B")
# x.add_edge("B", "C")
# x.add_edge("D", "C")

# print(x.shortest_path("A", "C"))


print('hi')

