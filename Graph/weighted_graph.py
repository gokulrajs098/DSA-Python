class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
    
    def addEdges(self, from_vertex, to_vertex, weight, is_Directed=False):
        self.add(from_vertex)
        self.add(to_vertex)

        self.graph[from_vertex][to_vertex] = weight
        if not is_Directed:
            self.graph[to_vertex][from_vertex] = weight

    def removeEdges(self, from_vertex, to_vertex):
        if from_vertex in self.graph and to_vertex in self.graph[from_vertex]:
            del self.graph[from_vertex][to_vertex]
        if to_vertex in self.graph and from_vertex in self.graph[to_vertex]:
            del self.graph[to_vertex][from_vertex]

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]

        for i in self.graph:
            if vertex in self.graph[i]:
                del self.graph[i][vertex]

wg = WeightedGraph()

wg.add("bengaluru")
wg.add("chennai")
wg.addEdges("bengaluru", "chennai", 300, True)

print(wg.graph)
wg.removeEdges("bengaluru", "chennai")
print(wg.graph)


wg.remove_vertex("chennai")
print(wg.graph)