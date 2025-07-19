
class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex in self.adjacency_list:
            raise Exception("Vertex already exists")
        self.adjacency_list[vertex] = []
        return self

    def add_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex1].append(vertex2)
        self.adjacency_list[vertex2].append(vertex1)
        return self

    def remove_edge(self, vertex1, vertex2):
        if vertex1 not in self.adjacency_list or vertex2 not in self.adjacency_list:
            raise Exception("Invalid vertices")
        self.adjacency_list[vertex1].remove(vertex2)
        self.adjacency_list[vertex2].remove(vertex1)
        return self

    #Time: O(V)
    #Space: O(1)

    def remove_vertex(self, vertex):
        if vertex not in self.adjacency_list:
            raise Exception("Vertex not found")
        for neighbor in self.adjacency_list[vertex]:
            self.adjacency_list[neighbor].remove(vertex)
        self.adjacency_list.pop(vertex)
        return self
        # Time: O(E)
        # Space: O(1)

new_graph = Graph() #Undirected graph
new_graph.add_vertex('A')
new_graph.add_vertex('B')
new_graph.add_vertex('C')
new_graph.add_edge('A','B')
new_graph.add_edge('A', 'C')
new_graph.add_edge('B', 'C')
new_graph.remove_vertex('A')
print(new_graph.adjacency_list)


