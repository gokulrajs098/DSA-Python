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

    def depth_first_traversal(self, start, alreadyVisited = set()):
        if start not in alreadyVisited:
            alreadyVisited.add(start)
            print(start, end=" ")
            for child in self.graph[start]:
                self.depth_first_traversal(child, alreadyVisited)

    def breath_first_traversal(self, start):
        alreadyVisited = {start}
        queue = [start]

        while len(queue)>0:
            current = queue.pop(0)
            print(current, end=" ") 

            for child in self.graph[current]:
                if child not in alreadyVisited:
                    queue.append(child)
                    alreadyVisited.add(child)
    
    def shortest_path(self, start, end):
        alreadyVisited = {start}
        queue = [(start, [start])]
        while len(queue)>0:
            current, path = queue.pop(0)
            for child in self.graph[current]:
                if child == end:
                    return path+[child]
                if child not in alreadyVisited:
                    queue.append((child, child+[path]))
                    alreadyVisited.add(child)
        return None
            
graph = Graph()

graph.addEdges("a", "b")
graph.addEdges("b", "c")
graph.addEdges("c", "d")
graph.addEdges("b", "d")

graph.depth_first_traversal("a")
graph.breath_first_traversal("a")
# graph.display()



    
            
    
