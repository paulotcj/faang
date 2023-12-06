# from typing import cast
#-------------------------------------------------------------------------
class NodeDist:
    #-------------------------------------------------------------------------
    def __init__(self, node, distance):
        self.node = node
        self.distance = distance
    #-------------------------------------------------------------------------
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
class ShortestDist
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
        self.data = {}
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
        for k, v in sorted_data.items():
            temp_str = ""
            sorted_v = sorted(v , key= lambda x: x.node )
            for i in sorted_v:
                temp_str += f"{i.node} (dist:{i.distance}), "

            print(f"Node {k} - Connects to: {temp_str}")
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
        g.print()


    #-------------------------------------------------------------------------

#-------------------------------------------------------------------------

mg_t = MyGraph_Dijkstra_Path_Test()
mg_t.test()

