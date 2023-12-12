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
def calculate_new_distance(graph, queue, distances, previous_nodes, curr_node, curr_distance):

    for neighbor, neighbor_distance in graph[curr_node].items():
        new_distance = curr_distance + neighbor_distance
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            previous_nodes[neighbor] = curr_node
            heapq.heappush(queue, (neighbor,new_distance))
    
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dijkstra(graph, start):
    #--------------------
    # prep
    queue = [(start, 0)]
    distances = {node: float('infinity') for node in graph} # creates a dictionary, the keys are the nodes in the graph, and the values are initially set to 'infinity'
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    #--------------------
    while queue:
        curr_node, curr_distance = heapq.heappop(queue)
        #-----
        if curr_distance <= distances[curr_node]:
            calculate_new_distance(graph = graph, queue = queue, distances = distances,
                                   previous_nodes = previous_nodes, curr_node = curr_node,
                                   curr_distance = curr_distance)
        #-----
    #end of while
    #--------------------
    return distances, previous_nodes
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


print('-------------------')

