import heapq
#-------------------------------------------------------------------------
def __explanation_and_collapsable():
    pass 
    # Consider the following graph with the distances between the parenteses:
    #       (5)
    #    A-------B
    #    |       |
    #    |(1)    |(2)
    #    |       |
    #    C-------D
    #       (8)
    #
    # And considering we are looking to find the shortest path from A to all different nodes, and ultimately we want to find the
    #  shortest path from A to D.
    # So we start by queueing A (in a priority queue ordered by distance), and we set the distance of A to 0.
    # We then examine all nodes connections (in this case all nodes connected to A), and we update the distance of the nodes connected to A.
    # We find that A is connected to B(5) and C(1)
    # Now we queue B and C to be checked next, and we also set a shortest path table.
    # Here's the representation of the priority queue (distance,node): (1, C) , (5, B)
    # And here's the representation of the shortest path table: {A: None, B: A, C: A, D: None}
    #
    # Now we pop the first node from the queue, C, and we examine its connections. It's connected to A(1) and D(8). For simplicity, we'll
    #  ignore A, since we already examined that path.
    # The connection to D has a distance of 8, and we update the distance of D to 9, since A --(1)--> C --(8)--> D = 9
    # Here's the representation of the priority queue (distance,node): (5, B), (9, D)
    # And here's the representation of the shortest path table: {A: None, B: A, C: A, D: C}
    #
    # Now we pop the first node from the queue, B, and we examine its connections. It's connected to A(5) and D(2). For simplicity, we'll
    #  ignore A, since we already examined that path.
    # The connection from B to D has a distance of 2, and we update the distance of D to 7, since A --(5)--> B --(2)--> D = 7
    # Here's the representation of the priority queue (distance,node): (7,D), (9, D)
    # And here's the representation of the shortest path table: {A: None, B: A, C: A, D: B}    
    #
    # Now we pop the first node from the queue, D, and we examine its connections. It's connected to B(2) and C(8). In this specific case, we
    #  know that we already explored the connections to B and C, so we can ignore them, but in reality the algorithm should still examine D's
    #  connections, since there might be connections to a new node that we haven't explored yet, thus leading to pottentionally shorter paths.
    #
    # In the end we explore the connections and confirm the shortest path from A to D is A --(5)--> B --(2)--> D = 7
    # And we can trace back the path from the shortest path table, consider the final result: {A: None, B: A, C: A, D: B}  
    # If we want to get the path from A to D, we start from D, and we can see the previous node is B, so we add B to the path, and then we see that
    #  B previous node is A.
    # The final path is D -> B -> A   Which can be easily reversed to A -> B -> D
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def add_edge(graph_dict, node1, node2, distance):
    #graph_dict is a dictionary of dictionaries
    if node1 not in graph_dict:
        graph_dict[node1] = {}
    if node2 not in graph_dict:
        graph_dict[node2] = {}

    graph_dict[node1][node2] = distance
    graph_dict[node2][node1] = distance
    # print(graph_dict)
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def calculate_new_distance(graph, queue, distances, path_table, inspecting_node, inspecting_node_distance):
    # the current distance is calculated from the perspective of the start node
    connections_to_curr_node = graph[inspecting_node]
    for neighbor, neighbor_distance in connections_to_curr_node.items(): #from the perspective of the current node, we connect the current shortest distance of this node to its neighbors, and check if we found a new shorter path
        new_distance = inspecting_node_distance + neighbor_distance  #new distance to the neighbor, perhapes we found a new shorter path?
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            path_table[neighbor] = inspecting_node
            heapq.heappush(queue, (new_distance, neighbor))
    
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

def shortest_path(graph, start, end):
    distances, previous_nodes = dijkstra(graph, start)
    path = []
    while end is not None:
        path.append([end, distances[end]])
        end = previous_nodes[end]
    return path[::-1]
#-------------------------------------------------------------------------	
	
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

graph = {}
add_edge(graph, "A", "B", 5)
add_edge(graph, "A", "C", 1)
add_edge(graph, "C", "B", 1)


print(dijkstra(graph, "A")[0]) # 0 = distances, 1 = previous_nodes - we only want the distances here

print(shortest_path(graph, "A", "B"))

print('-------------------')
# exit()

graph = {}
add_edge(graph, "A", "B", 5)
add_edge(graph, "A", "C", 1)

add_edge(graph, "B", "D", 2)
add_edge(graph, "C", "D", 8)



# print(dijkstra(graph, "A")[0]) # 0 = distances, 1 = previous_nodes - we only want the distances here

print(shortest_path(graph, "A", "D"))

print('-------------------')
# exit()


graph = {}
add_edge(graph, "A", "B", 6)
add_edge(graph, "A", "B", 6) # duplicate entry - added to test
add_edge(graph, "A", "B", 6) # duplicate entry - added to test
add_edge(graph, "A", "D", 1)
add_edge(graph, "B", "D", 2)
add_edge(graph, "B", "E", 2)
add_edge(graph, "B", "C", 5)
add_edge(graph, "D", "E", 1)
add_edge(graph, "E", "C", 5)

print(dijkstra(graph, "A")[0]) # 0 = distances, 1 = previous_nodes - we only want the distances here

print(shortest_path(graph, "A", "C"))

# exit()
print('-------------------')

graph = {}
add_edge(graph, "A", "B", 5)
add_edge(graph, "A", "C", 1)

add_edge(graph, "B", "D", 2)
add_edge(graph, "C", "D", 8)

add_edge(graph, "D", "E", 1)
add_edge(graph, "D", "F", 1)

add_edge(graph, "E", "G", 2)
add_edge(graph, "F", "G", 1)


print(dijkstra(graph, "A")[0]) # 0 = distances, 1 = previous_nodes - we only want the distances here

print(shortest_path(graph, "A", "G"))
print('-------------------')
# exit()









