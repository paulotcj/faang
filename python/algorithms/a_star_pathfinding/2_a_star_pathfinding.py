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
    def __calc_distance(self, a, b):
        (x1, y1) = self.element_locations[a]
        (x2, y2) = self.element_locations[b]
        return  math.sqrt( abs(x1 - x2)**2 + abs(y1 - y2)**2)
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def __find_heuristic(self, end):
        for e in self.graph:
            distance = self.__calc_distance(e, end)
            self.heuristic_distances[e] = distance
    #-------------------------------------------------------------------------    
    # #-------------------------------------------------------------------------
    # def add_edge(self, from_node, to_node):
    #     if from_node not in self.graph:
    #         self.graph[from_node] = {}
    #     self.graph[from_node][to_node] = self.__calc_distance(from_node, to_node)
    # #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def add_edge(self,from_node, to_node):
        #graph_dict is a dictionary of dictionaries
        if from_node not in self.graph:
            self.graph[from_node] = {}
        if to_node not in self.graph:
            self.graph[to_node] = {}

        distance = self.__calc_distance(from_node, to_node)

        self.graph[from_node][to_node] = distance
        self.graph[to_node][from_node] = distance
    #-------------------------------------------------------------------------            
    #-------------------------------------------------------------------------
    def a_star_search(self, start, end):
        priority_queue = []
        #---
        heapq.heappush(priority_queue, (0, start))
        came_from = { start: None}
        dist_so_far = {start: 0}
        #---
        while priority_queue:
            (curr_dist, current) = heapq.heappop(priority_queue)

            if current == end:
                break

            for next_node in self.graph[current]:
                new_distance = dist_so_far[current] + self.graph[current][next_node]
                if next_node not in dist_so_far or new_distance < dist_so_far[next_node]:
                    dist_so_far[next_node] = new_distance
                    heuristic = self.__calc_distance(next_node, end)
                    temp = new_distance + heuristic
                    heapq.heappush(priority_queue, (temp, next_node))
                    came_from[next_node] = current

        return came_from, dist_so_far
    #-------------------------------------------------------------------------
    #-------------------------------------------------------------------------
    def shortest_path(self, start, end):
        previous_nodes, distances  = self.a_star_search(start,end)
        path = []
        while end is not None:
            path.append([end, distances[end]])
            end = previous_nodes[end]
        return path[::-1]               
    #-------------------------------------------------------------------------    
#-------------------------------------------------------------------------
    
# print('----------------------------------')    
# graph = {}
# element_locations = { 'A': [1,1], 'B': [1,7] , 'C' : [7,7] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)
# x.add_edge("A", "B")
# x.add_edge("A", "C")
# x.add_edge("B", "C")

# print(x.shortest_path("A", "C"))    

# print('----------------------------------')    
# graph = {}
# element_locations = { 'A': [1,1], 'B': [1,7] , 'C' : [7,7], 'D': [1,8] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

# x.add_edge("A", "D")
# x.add_edge("A", "B")
# x.add_edge("B", "C")
# x.add_edge("D", "C")

# print(x.shortest_path("A", "C"))
    

# print('----------------------------------')

# graph = {}
# element_locations = { 'A': [1,1], 'B': [1,7] , 'C' : [7,7], 'D': [1,8] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

# x.add_edge("A", "D")
# x.add_edge("A", "B")
# x.add_edge("A", "C")
# x.add_edge("B", "C")
# x.add_edge("D", "C")

# print(x.shortest_path("A", "C"))   
    
# print('----------------------------------')

# graph = {}
# element_locations = { 'A': [1,1], 'B': [1,7] , 'C' : [7,7], 'D': [1,8], 'E': [4,4] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

# x.add_edge("A", "D")
# x.add_edge("A", "B")

# x.add_edge("A", "E")
# x.add_edge("E", "C")

# x.add_edge("B", "C")
# x.add_edge("D", "C")

# print(x.shortest_path("A", "C"))        


# print('----------------------------------')

# graph = {}
# element_locations = { 'A': [1,1], 'B': [2,7] , 'C' : [3,5], 'D': [4,8], 'E': [3,1], 'F' : [5,3], 
#                      'G': [6,6], 'H': [8,3], 'I':[8,6], 'J':[11,4] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

# x.add_edge("A", "E")
# x.add_edge("A", "B")

# x.add_edge("B", "C")

# x.add_edge("E", "C")

# x.add_edge("C", "F")
# x.add_edge("C", "D")

# x.add_edge("F", "H")

# x.add_edge("D", "G")

# x.add_edge("H", "J")
# x.add_edge("G", "I")
# x.add_edge("I", "J")



# print(x.shortest_path("A", "J"))  
    
# print('----------------------------------')

# graph = {}
# element_locations = { 'A': [1,1], 'B': [2,7] , 'C' : [3,5], 'D': [4,8], 'E': [3,1], 'F' : [5,3], 
#                      'G': [6,6], 'H': [8,3], 'I':[8,6], 'J':[11,4] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

# x.add_edge("A", "E")
# x.add_edge("A", "B")

# x.add_edge("A", "C")

# x.add_edge("B", "C")

# x.add_edge("E", "C")

# x.add_edge("C", "F")
# x.add_edge("C", "D")

# x.add_edge("F", "H")

# x.add_edge("D", "G")

# x.add_edge("H", "J")
# x.add_edge("G", "I")
# x.add_edge("I", "J")    

# print(x.shortest_path("A", "J"))  
    
# print('----------------------------------')

# graph = {}
# element_locations = { 'A': [1,1], 'B': [2,7] , 'C' : [3,5], 'D': [4,8], 'E': [3,1], 'F' : [5,3], 
#                      'G': [6,6], 'H': [8,3], 'I':[8,6], 'J':[11,4] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

# x.add_edge("A", "E")
# x.add_edge("A", "B")

# x.add_edge("A", "C")

# x.add_edge("B", "C")

# x.add_edge("E", "C")

# x.add_edge("C", "F")
# x.add_edge("C", "D")

# x.add_edge("F", "H")

# x.add_edge("D", "G")

# x.add_edge("H", "J")
# x.add_edge("G", "I")
# x.add_edge("I", "J")
# #--
# x.add_edge("G", "H")


# print(x.shortest_path("A", "J"))      

# print('----------------------------------')    

# graph = {}
# element_locations = { 'A': [1,1], 'B': [2,7] , 'C' : [3,5], 'D': [4,8], 'E': [3,1], 'F' : [5,3], 
#                      'G': [6,6], 'H': [8,3], 'I':[8,6], 'J':[11,4] }


# x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

# x.add_edge("A", "E")
# x.add_edge("A", "B")

# x.add_edge("A", "C")

# x.add_edge("B", "C")

# x.add_edge("E", "C")

# x.add_edge("C", "F")
# x.add_edge("C", "D")

# x.add_edge("F", "H")

# x.add_edge("D", "G")

# x.add_edge("H", "J")
# x.add_edge("G", "I")
# x.add_edge("I", "J")
# #--
# x.add_edge("G", "H")
# x.add_edge("E", "F")


# print(x.shortest_path("A", "J"))   
    
print('----------------------------------')

graph = {}
element_locations = { 'A': [1,1], 'B': [2,7] , 'C' : [3,5], 'D': [4,8], 'E': [3,1], 'F' : [5,3], 
                     'G': [6,6], 'H': [8,3], 'I':[8,6], 'J':[11,4] }


x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)

x.add_edge("A", "E")
x.add_edge("A", "B")

x.add_edge("A", "C")

x.add_edge("B", "C")

x.add_edge("E", "C")

x.add_edge("C", "F")
x.add_edge("C", "D")

x.add_edge("F", "H")

x.add_edge("D", "G")

x.add_edge("H", "J")
x.add_edge("G", "I")
x.add_edge("I", "J")
#--
x.add_edge("G", "H")
x.add_edge("E", "F")
#--

x.add_edge("B", "D")
x.add_edge("F", "G")
x.add_edge("H", "I")
x.add_edge("D", "F")




print(x.shortest_path("A", "J"))       
        

print('----------------------------------')

graph = {}
element_locations = { 'A': [1,1], 'B': [3,1] , 'C' : [5,1], 'D': [6,3], 'E': [7,1], 'F' : [8,3], 
                     'G': [9,1], 'H': [10,4], 'I':[11,1], 'J':[12,4], 'K':[13,1],
                      'L':[6,5], 'M':[13,5] }
x = A_Star_Pathfinding(graph=graph, element_locations=element_locations)    

x.add_edge("A", "B")
x.add_edge("B", "C")
x.add_edge("C", "D")
x.add_edge("D", "E")
x.add_edge("E", "F")
x.add_edge("F", "G")
x.add_edge("G", "H")
x.add_edge("H", "I")
x.add_edge("I", "J")
x.add_edge("J", "K")

x.add_edge("A", "L")
x.add_edge("L", "M")
x.add_edge("M", "K")

print(x.shortest_path("A", "K"))   


print('END')        