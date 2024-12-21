class Graph:
    def __init__(self):
        self.graph = {}
        
    def addVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print("vertex already exists")
    
    def addEdges(self, vertex1, vertex2, isDirected=False):
        self.addVertex(vertex1)
        self.addVertex(vertex2)
        self.graph[vertex1].append(vertex2)
        if isDirected:
            self.graph[vertex2].append(vertex1)

    def display(self):
        for key, value in self.graph.items():
            print(f"{key} => {value}")
    
    def getVertices(self):
        for i in self.graph:
            print(i)
    
    def getEdges(self):
        for key, value in self.graph.items():
            for vertex in value:
                print(f"({key}, {vertex})")

    def removeVertex(self, vertex):
        if vertex in self.graph:
            del self.graph[vertex]
            for key, value in self.graph.items():
                if vertex in value:
                    value.remove(vertex)

    def isEdge(self, vertex1, vertex2):
        return vertex1 in self.graph[vertex2] or vertex2 in self.graph[vertex1]
    
    def removeEdges(self, vertex1, vertex2):
        if self.isEdge(vertex1, vertex2):
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)

graph = Graph()

graph.addEdges("a", "b")
graph.addEdges("b", "a")
graph.addEdges("a", "d")
graph.addEdges("b", "c")
graph.addEdges("c", "a")
graph.addEdges("d", "a")



graph.removeVertex("c")
graph.removeEdges("a", "b")
graph.display()

graph.getVertices()

graph.getEdges()