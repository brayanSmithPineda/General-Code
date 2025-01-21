"""
A graph is a data structura that consist of a set of nodes and a set of adges that connet pairs of nodes.
Undirect graph: Edges have no direction. if there is an edge between A and B, you can go from A to B and from B to A
Direct graph: Edges have direction. if there is a directe edge from A to B you can not go from B to A

Graph can be represent it by adjacency matrix and adjacency list
"""

"""
- Undirect Graph
    0
   / \
  1---2

Adjacency Matrix: In an adjacency matrix, we use a 2D array (a list of lists in Python) where matrix[i][j] is 1 (or True) if there is an edge from node i to node j, and 0 (or False) otherwise.

# 0  1  2
[[0, 1, 1],  # 0
 [1, 0, 1],  # 1
 [1, 1, 0]]  # 2

Adjacency List:
1-Using a dict
{
0: [1,2],
1: [0,2],
2: [0,1]
}
2- Using a list of list
[
[1,2],
[0,2],
[0,1]
]
Direct graph representation
    0
    |
    v
    1 --> 2
# 0  1  2
[[0, 1, 0],  # 0
 [0, 0, 1],  # 1
 [0, 0, 0]]  # 2

 Note: You always see the rows and then the columns
 matrix[i][j] = 1 indicates a direct edge from vertex i to vertex j.

Adjacency list
{
0: [1],
1: [2],
2:[]
} 

[[1],[2],[]]
"""

#Implementation 
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, source_node, destination_node):
    #The intention is to create an edge going from src to dest
    # Assuming that the source node already exists in the graph,
    # we add the destination node to the adjacency list of the source node.
        if source_node in self.adj_list:#The intention is to create an edge going from src to dest
            self.adj_list[source_node].append(destination_node)
    # For an undirected graph, you would also add the reverse edge from dest to src.


    def print_graph(self):
        for vertex in self.adj_list:
            print(f"{vertex} -> {self.adj_list[vertex]}")

# Create the graph instance
graph = Graph()

# Add vertices
for vertex in [12, 17, 18, 29, 30]:
    graph.add_vertex(vertex)

# Add edges based on the directed graph structure
graph.add_edge(12, 17)
graph.add_edge(17, 18)
graph.add_edge(18, 29)
graph.add_edge(29, 30)
graph.add_edge(30, 12)

# Print the graph
graph.print_graph()

class Graph: 
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, source_node, destination_node):
        if source_node in self.graph and destination_node in self.graph:
            self.graph[source_node].append(destination_node)
            # self.graph[destination_node].append(source_node) undirected graph

    def print_graph(self):
        for node in self.graph:
            print(f"{node} --->{self.graph[node]}")


class GraphMatrix:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.graph = [[0]*num_nodes for _ in range(num_nodes)]        
    
    # def add_node() There is no method to add a node because we fixed the matrix in the constructor we already know that we are going to have a tree with num_nodes, the matrix only holds 1 is there is an egde 0 otherwise.
    
    def add_edge(self, src_index_node, dest_index_node):#here src and dest are not nodes but the index that are in the range of the matrix, we have to assing each node a corresponding index so we can mapp the matrix.
        if 0 <= src_index_node < self.num_nodes and 0 <= dest_index_node < self.num_nodes:
            self.graph[src_index_node][dest_index_node] = 1 
            # self.graph[dest_index_node][src_index_node] = 1 *indirected graph

    def print_graph(self):
        for row in self.graph:
            print(row)

num_nodes = 5  # Number of nodes
graph_matrix = GraphMatrix(num_nodes)

# Add edges
graph_matrix.add_edge(0, 1)
graph_matrix.add_edge(1, 2)
graph_matrix.add_edge(2, 3)
graph_matrix.add_edge(3, 4)
graph_matrix.add_edge(4, 0)  # Adding an edge back to the starting node for demonstration

graph_matrix.print_graph()
