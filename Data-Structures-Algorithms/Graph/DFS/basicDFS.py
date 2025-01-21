"""Iterative approach using and adjacency list"""

class Graph:
    def __init__(self):
        self.adj_list = {}
    def add_node(self, node):
        self.adj_list[node] = []
    def add_edge(self, src, dest):
        if src in self.adj_list and dest in self.adj_list:
            self.adj_list[src].append(dest)
    
def dfs_iterative(adj_list, node): #The inputs are the graph, and the starting node where we need to start the the DFS
    visited = set()
    stack = [node] #Intead of a queue we use a stack as we need to pop from the last position
    while stack:
        node = stack.pop() #We pop from the last position that we we can go in depth in a branch
        if node not in visited:
            visited.add(node)
            print(node) #In real applicantions we could do more that just printing the node, maybe check some condition or anything else
            if node in adj_list: #This is assuming that some nodes my not be part of our graph, is just a saveguard to avoid keyErrors
                for neighbors in adj_list[node]:
                    if neighbors not in visited:
                        stack.append(neighbors)

def dfs_recursive(adj_list, node, visited = None):#If you define visited inside the recursive function without passing it along, each recursive call would have its own separate visited set, losing the state of which nodes have been visited in other branches of the recursion.Passing visited as an argument ensures that all recursive calls share the same visited state, allowing the function to correctly track which nodes have been visited across the entire traversal.
    if visited is None: #If visited is None then we create the variable to keep track of the visited nodes, this is just doing at the beggining because in the subsequence function visited will be not none
        visited = set()
    
    if node not in visited:
        visited.add(node)
        print(node)
        if node in adj_list:
            for neighbors in adj_list[node]:
                if neighbors not in visited:
                    dfs_recursive(adj_list, neighbors, visited)