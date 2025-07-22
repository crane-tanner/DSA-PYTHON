from collections import deque


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


    def breadth_first_traversal(self, start_vertex):  # Time: O(V+E) Space: O(V)
        if start_vertex not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        queue = deque()
        queue.append(start_vertex)
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list} # dictionary comprehension
        explored[start_vertex] = True
        while queue:
            current = queue.popleft()
            visited.append(current)
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    queue.append(adjacent)
                    explored[adjacent] = True
        return visited

    def dft_iterative(self, start_vertex):  # Time: O(V+E) Space: O(V)
        if start_vertex not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        stack = [start_vertex]
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}  # dictionary comprehension
        explored[start_vertex] = True
        while stack:
            current = stack.pop()
            visited.append(current)
            for adjacent in self.adjacency_list[current]:
                if not explored[adjacent]:
                    stack.append(adjacent)
                    explored[adjacent] = True
        return visited
    # Using stack container to visit nodes instead of queue in dft_iterative

    def dft_recursive(self, start_vertex): # Time: O(V+E) Space: O(V)
        if start_vertex not in self.adjacency_list:
            raise Exception("Vertex not in graph")
        visited = []
        explored = {vertex: False for vertex in self.adjacency_list}  # dictionary comprehension

        def _traversal(current):
            visited.append(current)
            explored[current] = True
            for adjacent in self.adjacency_list:
                if not explored[adjacent]:
                    _traversal(adjacent)
            return
        _traversal(start_vertex)
        return visited


new_graph = Graph() #Undirected graph
new_graph.add_vertex('A')
new_graph.add_vertex('B')
new_graph.add_vertex('C')
new_graph.add_vertex('D')
new_graph.add_edge('A','B')
new_graph.add_edge('A', 'C')
new_graph.add_edge('B', 'C')
new_graph.add_edge('C', 'D')
new_graph.add_edge('A', 'D')
print(new_graph.adjacency_list)


