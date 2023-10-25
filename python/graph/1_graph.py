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
        for i in self.adcent_list:
            print(f'i: {i} --> {self.adcent_list[i]}')

#------------------------------------------------------------

x = Graph()
x.add_vertex('0')
x.add_vertex('1')
x.add_vertex('2')
x.add_vertex('3')
x.add_vertex('4')
x.add_vertex('5')
x.add_vertex('6')

x.add_edge('3', '1') 
x.add_edge('3', '4') 
x.add_edge('4', '2') 
x.add_edge('4', '5') 
x.add_edge('1', '2') 
x.add_edge('1', '0') 
x.add_edge('0', '2') 
x.add_edge('6', '5')

x.show_connections()