# from typing import cast
#-------------------------------------------------------------------------
class NodeDist:
    #-------------------------------------------------------------------------
    def __init__(self, node, distance):
        self.node = node
        self.edge_distance = distance
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class ShortestDist:
    #-------------------------------------------------------------------------
    def __init__(self, dist, prev):
        self.shortest_distance = dist
        self.prev = prev
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class MyGraph_Dijkstra_Path:
    #-------------------------------------------------------------------------
    def __explanation_and_collapsable():
        pass 
        # Algorithm:
        # Let distance of start vertex from start vertex = 0
        # Let distance of all other vertices from start = infinity (in this example we simply dont have them in the list)
        # 
        # Repeat:
        #    Visit the unvisited vertez with the smallest known distance from the start vertex
        #    For the current vertex, examine its unvisited neighbours
        #    For the current vertex, calculate distance of each neighbour from start vertex
        #    If the calculated distance of a vertex is less than the know distance, update the shortest distance
        #    Update the previous vertez for each of the updated distances
        #    Add the current vertez to the list of visited vertices
        # until all vertices visited    
    #-------------------------------------------------------------------------
    def __init__(self):
        self.data = {} #dict
        self.q = [] # list
        self.distance_table = {} #dict
    #-------------------------------------------------------------------------        
    #-------------------------------------------------------------------------
    def __add_vertex(self, node):
        if node not in self.data:
            self.data[node] = []
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def add_edge(self, node1, node2, distance):
        self.__add_vertex(node1)
        self.__add_vertex(node2)
        #---
        node1_dist = NodeDist(node1,distance)
        node2_dist = NodeDist(node2,distance)
        #---
        
        # entry_exists = True if node2 in self.data[node1] else False
        entry_exists = [node_i for node_i in self.data[node1] if node_i.node == node2 ]
        if len(entry_exists) == 0 and node1 != node2:
            self.data[node1].append(node2_dist)
        #---
        # entry_exists = True if node1 in self.data[node2] else False
        entry_exists = [node_i for node_i in self.data[node2] if node_i.node == node1 ]
        if len(entry_exists) == 0 and node1 != node2:
            self.data[node2].append(node1_dist)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def print(self):
        sorted_data = dict(sorted(self.data.items()))
        return_result = []
        for k, v in sorted_data.items():
            temp_str = ""
            sorted_v = sorted(v , key= lambda x: x.node )
            for i in sorted_v:
                temp_str += f"{i.node} (dist:{i.edge_distance}), "

            temp_str = f"Node {k} - Connects to: {temp_str}"
            return_result.append(temp_str)
            print(temp_str)
        
        return return_result
    #-------------------------------------------------------------------------
    def __calculate_distance_table(self, current_node):
        current_node_dist = self.distance_table[current_node]
        current_node_connections = self.data[current_node] #get a list with all connections for the node which we are accessing

        for child in current_node_connections:
            #The options below are simple, we need to identify:
            # 1 - is there a previous path?
            #      if so, is the distance of this path shorter than the existing distance?
            # 2 - If no previous path is found, add one

            if  child.node in self.distance_table:

                # we need to update the existing reference if the added distance of the current node and its previous node is less than
                # the distance of the existing conn
                path_so_far = self.distance_table[child.node]

                # sum the shortest path so far, and add the distance of the current edge 
                sum_distances = (path_so_far.shortest_distance + child.edge_distance)

                # did we find a shorter path? if yes update!
                if current_node_dist.shortest_distance > sum_distances:
                    current_node_dist.shortest_distance = sum_distances #updated new shorter distance
                    current_node_dist.prev = child.node #the shortest path now is taken through the current child node
                    
                    # self.distance_table[current_node] = current_node_dist

                    # if the shortest distance of this path is altered we need to reevaluate all paths connected to this path
                    #  therefore, we need to enqueue again
                    self.q.append(current_node)
                #---------
            else: #no previous path exists
                # add the distances ( current distance + shortest distance so far)
                #   and then add the current node being inspected to que queue
                sum_distances = child.edge_distance + current_node_dist.shortest_distance
                self.distance_table[child.node] = ShortestDist(dist=sum_distances, prev= current_node)
                self.q.append(child.node)
            #---------
        #end of for loop
        #---------
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def dijkstra(self, param_start):
        self.start = param_start
        self.q = []
        # self.data = {}
        self.distance_table = {}

        # current = None
        self.q.append(param_start)
        self.distance_table[param_start] = ShortestDist(dist=0, prev=param_start)

        while self.q:
            # print(f"printing the queue")
            # print(self.q)

            current = self.q.pop(0)
            #calculate distance table for current
            self.__calculate_distance_table(current) #this step is far too complicated so it is better to place it in a separate place
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def print_distance_table(self):
        return self.__print_distance_table(self.distance_table)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __print_distance_table(self, param_distance_table):
        if param_distance_table == None: return
        return_result = []

        param_distance_table = dict(sorted(param_distance_table.items()))

        for k, v in param_distance_table.items():
            temp_str = f"Vertex: {k} - Shortest Distance: {v.shortest_distance} - Previous vertex: {v.prev}"
            print(temp_str)
            return_result.append(temp_str)

        return return_result        
    #-------------------------------------------------------------------------    
    #-------------------------------------------------------------------------
    def find_shortest_path_to(self, endpoint):
        select = None
        prev = None
        shortest_path_route = []
        while True:
            prev = select
            select = {endpoint : self.distance_table[endpoint]}
            shortest_path_route.append([endpoint, self.distance_table[endpoint].shortest_distance])
            
            if self.distance_table[endpoint].shortest_distance == 0:
                # self.__print_distance_table(select)
                break
            
            # self.__print_distance_table(select)
            endpoint = self.distance_table[endpoint].prev
        #end of while loop
        #---------
        return shortest_path_route
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def input_data_from_matrix(self, headers_list, connection_matrix, distance_matrix):
        for header_i in range(len(headers_list)):
            node_1 = headers_list[header_i] 

            for conn_i in range(len(connection_matrix[header_i])):
                target_connection = connection_matrix[header_i][conn_i]
                if  target_connection == 1:
                    node_2 = headers_list[conn_i]
                    distance = distance_matrix[header_i][conn_i]
                    self.add_edge(node1 = node_1, node2= node_2, distance= distance)            
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class MyGraph_Dijkstra_Path_Test:
    #-------------------------------------------------------------------------
    def test(self):

        #---------------------------------------

        #    A-------B
        #    |     / |  \ 
        #    |   /   |    C
        #    | /     |  /
        #    D-------E

        #       (6)
        #    A-------B
        #    | (2) / |  \(5)
        # (1)|   /   |    C
        #    | /  (2)|  /(5)
        #    D-------E
        #       (1)

        g = MyGraph_Dijkstra_Path()
        g.add_edge("A", "B", 6)
        g.add_edge("A", "D", 1)
        g.add_edge("B", "D", 2)
        g.add_edge("B", "E", 2)
        g.add_edge("B", "C", 5)
        g.add_edge("D", "E", 1)
        g.add_edge("E", "C", 5)

        connections_expected_result = [
            "Node A - Connects to: B (dist:6), D (dist:1), ",
            "Node B - Connects to: A (dist:6), C (dist:5), D (dist:2), E (dist:2), ",
            "Node C - Connects to: B (dist:5), E (dist:5), ",
            "Node D - Connects to: A (dist:1), B (dist:2), E (dist:1), ",
            "Node E - Connects to: B (dist:2), C (dist:5), D (dist:1), "
        ]
        print("Analyzing the graph:")
        connection_result = g.print()

        print(f"\nDoes the summary results match the expected results? Answer: {connection_result == connections_expected_result}")
        
        
        print("-------")

        shortest_distance_table_expected_result = [
            "Vertex: A - Shortest Distance: 0 - Previous vertex: A",
            "Vertex: B - Shortest Distance: 3 - Previous vertex: D",
            "Vertex: C - Shortest Distance: 7 - Previous vertex: E",
            "Vertex: D - Shortest Distance: 1 - Previous vertex: A",
            "Vertex: E - Shortest Distance: 2 - Previous vertex: D",
        ]


        g.dijkstra(param_start="A")
        print("Dijkstra distance table\n(Note we can derive a route considering the origin from 'A' ):\n")
        shortest_distance_table_result = g.print_distance_table()

        print(f"\nDoes the summary results match the expected results? Answer: {shortest_distance_table_result == shortest_distance_table_expected_result}")
        print("-------")
        route_expected_result = [
            ['C', 7],
            ['E', 2],
            ['D', 1],
            ['A', 0]
        ]        
        route_result = g.find_shortest_path_to("C")
        print(f"Result for the shortest path from A to C: {route_result}")
        print(f"Does the summary results match the expected results? Answer: {route_result == route_expected_result}")
        print("-------")

        #---------------------------------------
        # Matrix representation of the graph
        #    A-------B
        #    |     / |  \ 
        #    |   /   |    C
        #    | /     |  /
        #    D-------E

        #       (6)
        #    A-------B
        #    | (2) / |  \(5)
        # (1)|   /   |    C
        #    | /  (2)|  /(5)
        #    D-------E
        #       (1)

        #     A  B  C  D  E
        #  A  1  1  0  1  0        
        #  B  1  1  1  1  1    
        #  C  0  1  1  0  1    
        #  D  1  1  0  1  1    
        #  E  0  1  1  1  1  
        
        nodes_list = ["A", "B", "C", "D", "E" ]  
        nodes_connections = [
            #A   B   C   D   E
            [1,  1,  0,  1,  0], # A
            [1,  1,  1,  1,  1], # B
            [0,  1,  1,  0,  1], # C
            [1,  1,  0,  1,  1], # D
            [0,  1,  1,  1,  1]  # E       
        ]

        #Note: -1 distances are for nodes that are not connected
        nodes_distance = [
              #A   B   C   D   E
            [  0,  6, -1,  1, -1 ], # A
            [  6,  0,  5,  2,  2 ], # B
            [ -1,  5,  0, -1,  5 ], # C
            [  1,  2, -1,  0,  1 ], # D
            [ -1,  2,  5,  1,  0 ]  # E         
        ]

        #Let's start a new graph
        g = MyGraph_Dijkstra_Path()
        g.input_data_from_matrix(headers_list = nodes_list, connection_matrix = nodes_connections,
                                 distance_matrix = nodes_distance)
        
        print("Matrix representation of the graph")
        matrix_connection_result = g.print()
        print(f"Does the summary results match the expected results? Answer: {matrix_connection_result == connections_expected_result}")
        print("-------")


        g.dijkstra(param_start="A")
        print("Dijkstra distance table (USING MATRICES)\n(Note we can derive a route considering the origin from 'A' ):\n")
        matrix_shortest_distance_table_result = g.print_distance_table()

        print(f"\nDoes the summary results match the expected results? Answer: {matrix_shortest_distance_table_result == shortest_distance_table_expected_result}")
        print("-------")  

        matrix_route_result = g.find_shortest_path_to("C")
        print(f"(Matrix) Result for the shortest path from A to C: {route_result}")
        print(f"Does the summary results match the expected results? Answer: {matrix_route_result == route_expected_result}")
        print("-------")              

           


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

mg_t = MyGraph_Dijkstra_Path_Test()
mg_t.test()

