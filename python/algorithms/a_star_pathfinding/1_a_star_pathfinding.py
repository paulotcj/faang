import heapq
import math


#-------------------------------------------------------------------------
class A_Star_Pathfinding:
    #-------------------------------------------------------------------------
    def __calc_distance(self, node1, node2):
        dist1 = node2[0] - node1[0]
        dist2 = node2[1] - node1[1]
        dist = math.sqrt(dist1**2 + dist2**2)
        return dist
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def add_edge(self,graph_dict, node1, node2, locations):
        #graph_dict is a dictionary of dictionaries
        if node1 not in graph_dict:
            graph_dict[node1] = {}
        if node2 not in graph_dict:
            graph_dict[node2] = {}

        distance = self.__calc_distance(locations[node1], locations[node2])

        graph_dict[node1][node2] = {'edge': distance, 'heuristic': float('infinity')}
        graph_dict[node2][node1] = {'edge': distance, 'heuristic': float('infinity')}
        # print(graph_dict)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dijkstra(graph, start):
        #--------------------
        # prep
        queue = [(0, start)]
        distances = {node: float('infinity') for node in graph} # creates a dictionary, the keys are the nodes in the graph, and the values are initially set to 'infinity'
        distances[start] = 0
        path_table = {node: None for node in graph}
        #--------------------
        while queue:
            inspecting_node_distance, inspecting_node = heapq.heappop(queue)
            #-----
            saved_distance = distances[inspecting_node]
            if inspecting_node_distance <= saved_distance: # even if its the same distance, we still want to process it, because we might find a shorter path down the road
                calculate_new_distance(graph = graph, queue = queue, distances = distances,
                                    path_table = path_table, inspecting_node = inspecting_node,
                                    inspecting_node_distance = inspecting_node_distance)
            #-----
        #end of while
        #--------------------
        return distances, path_table
    #-------------------------------------------------------------------------


#-------------------------------------------------------------------------

graph = {}
element_locations = { 'A': [1,1], 'B': [1,7] , 'C' : [7,7] }


x = A_Star_Pathfinding()
x.add_edge(graph, "A", "B", element_locations)
x.add_edge(graph, "A", "C", element_locations)
x.add_edge(graph, "B", "C", element_locations)

print('hi')

