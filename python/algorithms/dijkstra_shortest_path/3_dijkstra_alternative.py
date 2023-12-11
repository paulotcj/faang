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
#-------------------------------------------------------------------------
#-------------------------------------------------------------------------
def dijkstra(graph, start):
    #--------------------
    # prep
    queue = [(0, start)]
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    #--------------------
    while queue:
        (distance, current_node) = heapq.heappop(queue)
        if distance <= distances[current_node]:
            for neighbor, neighbor_distance in graph[current_node].items():
                new_distance = distance + neighbor_distance
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(queue, (new_distance, neighbor))
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

print(dijkstra(graph, "A")) 

print(shortest_path(graph, "A", "C"))


print('-------------------')

