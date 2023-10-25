

class Graph:
    def __init__(self) -> None:
        self.number_nodes = 0
        self.adcent_list = {}
        
    def add_vertex(self,node):
        self.adcent_list[node] = []
        self.number_nodes += 1
    
    def add_edge(self,node1, node2):
        self.adcent_list[node1].append(node2)
        self.adcent_list[node2].append(node1)
    
    def show_connections(self):
        pass