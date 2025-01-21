"""
BFS in Graphs:
    -Cycles and Multiple Paths: Graphs can have cycles and multiple paths between nodes,  so it's crucial to track which nodes have been visited to prevent infinite loops and redundant processing.

    -Arbitrary Starting Point: Unlike trees, BFS in a graph can start from any node, not just a root (since the concept of a root doesn't exist in general graphs).

    -Implementation: The BFS for a graph includes a visited set to track which nodes have been explored. This set ensures that each node is processed only once.
"""


from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}  # Dictionary to store the graph

    def add_edge(self, src, dest):
        # Adding the node to the graph
        if src not in self.graph:
            self.graph[src] = []
        if dest not in self.graph:
            self.graph[dest] = []

        # Adding the edge
        self.graph[src].append(dest)
        
        def BFS(self, start_node):
            if not start_node:
                return 
            
            visited_nodes = set() #nodes in a graph can have circular references and in general there is more that one way to get to a node, for that reason you have to keep track of the nodes that have already been visited so you do not processe it again
            # queue = [start_node]
            queue = deque([start_node]) #Here we just add the start_node to the queue, we are Using deque for efficient popping from the left that process we have to make it later

            while queue:
                # vertex = queue.pop(0) ---O(n) time complexity
                vertex = queue.popleft() #O(1) time complexity
                if vertex not in visited_nodes:
                    print(vertex.data) #In a real-world application, instead of printing each vertex, you might perform some other operation on the node, such as checking if it meets a certain condition or processing its data in some way.
                    visited_nodes.add(vertex)
                
                for neighbors in self.graph[vertex]: #self.graph[vertex] is a list of the neighbors related to the vertex
                    if neighbors not in visited_nodes:
                        queue.append(neighbors)
    
from collections import deque

class GraphMatrix:
    def __init__(self, size):
        # Initialize the adjacency matrix with all 0's
        self.matrix = [[0]*size for _ in range(size)]
    
    def add_edge(self, src, dest):
        # Add an edge from src to dest
        self.matrix[src][dest] = 1
        # If it's an undirected graph, uncomment the next line
        # self.matrix[dest][src] = 1
    
    def BFS(self, start_vertex):
        # Initialize all vertices as not visited
        visited = [False] * len(self.matrix) #This is 1D List or Array representing the nodes or vertices, remember that althoug we have a matrix each element of the matrix represent an edge and not a node, that's why if we a 3x3 matrix that means we have just 3 nodes so the visited array is going to be a list of 3 elements.
        
        # Create a queue for BFS
        queue = deque()
        
        # Mark the start vertex as visited and enqueue it
        visited[start_vertex] = True
        queue.append(start_vertex)
        
        while queue:
            # Dequeue a vertex from the queue and print it
            vertex = queue.popleft()
            print(vertex, end=" ")
            
            # Get all adjacent vertices of the dequeued vertex
            # If an adjacent vertex has not been visited, mark it visited and enqueue it
            for i in range(len(self.matrix)): #Here we loop in an nxn matrix 0 to n-1, this ensure we visit all the elements in the list of the vertex, remember here we are seeing edge not nodes, that's why we have to make sure self.matrix[vertex][1] == 1 that means vertex i is a neighbor of vertex so we have to added to the queue if it has not been visited.
                if self.matrix[vertex][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

# Example Usage
g = GraphMatrix(4)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("BFS starting from vertex 2:")
g.BFS(2)

matrix = [
    [1,2,3],
    [4,5,6],
    [6,7,8]
]
length = len(matrix)
length
b = [False]*len(matrix)
b