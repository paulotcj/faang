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
        entry_exists = True if node2 in self.data[node1] else False
        if entry_exists == False:
            self.data[node1].append(node2_dist)
        #---
        entry_exists = True if node1 in self.data[node2] else False
        if entry_exists == False:
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
                if child.node == 'B':
                    print('debug')
                # we need to update the existing reference if the added distance of the current node and its previous node is less than
                # the distance of the existing conn
                path_so_far = self.distance_table[child.node]

                # sum the shortest path so far, and add the distance of the current edge 
                sum_distances = (path_so_far.shortest_distance + child.edge_distance)

                # did we find a shorter path? if yes update!
                if current_node_dist.shortest_distance > sum_distances:
                    current_node_dist.shortest_distance = sum_distances #updated new shorter distance
                    current_node_dist.prev = current_node #the shortest path now is taken through the current child node
                    
                    self.distance_table[current_node] = current_node_dist

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
            print(f"printing the queue")
            print(self.q)

            current = self.q.pop(0)
            #calculate distance table for current
            self.__calculate_distance_table(current) #this step is far too complicated so it is better to place it in a separate place
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def print_distance_table(self):
        if self.distance_table == None: return

        for k, v in self.distance_table.items():
            print(f"Vertex: {k} - Shortest Distance: {v.shortest_distance} - Previous vertex: {v.prev} ")
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

        expected_result = [
            "Node A - Connects to: B (dist:6), D (dist:1), ",
            "Node B - Connects to: A (dist:6), C (dist:5), D (dist:2), E (dist:2), ",
            "Node C - Connects to: B (dist:5), E (dist:5), ",
            "Node D - Connects to: A (dist:1), B (dist:2), E (dist:1), ",
            "Node E - Connects to: B (dist:2), C (dist:5), D (dist:1), "
        ]
        result = g.print()
        print("-------")
        print(f"Does the summary results match the expected results? Answer: {result == expected_result}")
        print("-------")
        g.dijkstra(param_start="A")
        g.print_distance_table()


    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------

mg_t = MyGraph_Dijkstra_Path_Test()
mg_t.test()

