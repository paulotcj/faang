import heapq

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









