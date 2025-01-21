class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def bfs_level_order_traversal(root):
    if not root:
        return []
    
    result = []
    queue = [root]  # Initialize queue with root
    
    while queue:
        level_size = len(queue)  # Number of elements in the current level, this is use to define how many time the for loop iterates, the foor loop iterates over a level of nodes, the root only have one node so the for loop so iterate one time.

        current_level = []  # List to store nodes at the current level, this is use to store the elements of the current level, so for the root it just one element that then is pass to the result list
        
        for _ in range(level_size):#Loop through the number of element that are in queue, this are the nodes in a specif level
            node = queue.pop(0)  # we Dequeue or pop the first element of the queue, and save it a varaible node to put it later in the current_level list that stores the nodes in a specific level
            current_level.append(node.value)  # We save the data or value of the node we just delete
            
            # if the delete node we just put in the current_level have childrens then we append them at them end of the queue so the next time we enter the for loop we procese them as well
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)  # After we exit the for loop we sucessfully append the nodes in certain level in the result, this variable is going to store all the sublists that contains the nodes in all the levels of the tree
    
    return result
"""
        3
       / \
      9   20
         /  \
        15   7
"""
"""
Algorithm 
1-Initialization:
    -We start with the root node 3. The queue initially contains this node: queue = [3].
2-First Iteration (Level 1):

    -We enter the while loop because queue is not empty.
    -level_size is 1 because there's only one node at this level (the root node 3).
    -We initialize an empty list current_level to store nodes' values at this level.
    -We go into a for loop which runs only once (since level_size is 1).
        -Dequeue node 3 from the queue: queue = [].
        -Add node 3's value to current_level: current_level = [3].
        -Enqueue node 3's children (9 and 20) to the queue: queue = [9, 20].
    -After the loop, we add current_level to result: result = [[3]].
3-Second Iteration (Level 2):

    -Now, queue = [9, 20] and level_size = 2.
    -Reset current_level = [].
    -In the for loop (which runs twice now):
        -Dequeue node 9 (first iteration): queue = [20].
            -current_level becomes [9].
            -Node 9 has no children, so nothing is enqueued.
        -Dequeue node 20 (second iteration): queue = [].
            -current_level becomes [9, 20].
            -Enqueue node 20's children (15 and 7): queue = [15, 7].
    -Add current_level to result: result = [[3], [9, 20]].
4-Third Iteration (Level 3):

    -Now, queue = [15, 7] and level_size = 2.
    -Reset current_level = [].
    -Again, the for loop runs twice:
        -Dequeue node 15 (first iteration): queue = [7].
            -current_level becomes [15].
            -Node 15 has no children, so nothing is enqueued.
        -Dequeue node 7 (second iteration): queue = [].
            -current_level becomes [15, 7].
            -Node 7 also has no children, so nothing is enqueued.
    -Add current_level to result: result = [[3], [9, 20], [15, 7]].
5Completion:
    -Now, queue is empty, so we exit the while loop.
    -The result now holds the level order traversal of the tree: [[3], [9, 20], [15, 7]].
    -This final result list represents the tree's level order traversal, showing which -nodes are on each level of the tree.

"""

class Tree:
    def __init__(self, data):
        self.data = data
        self.childrens = []

def BFS(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current_level_nodes = []
        size = len(queue) #we use a varaible to store the len to know how many time the foor loop should iterate, we do not use the len directly in the for loop beacuase every time we pop from the queue the length change that's why we have to save it before the loo
        for _ in range(size): # we use _ in the foor loop because we really didn't use it
            node = queue.pop(0)
            current_level_nodes.append(node.data) #we append the data of the node

            for j in node.childrens:
                queue.append(j) #Here you have to append the node beacause later you need to access its childrens, if you append the j.data then you can not access the children property of the constructor
        result.append(current_level_nodes)
    return result    

root = Tree(5)
child1 = Tree(1)
child2 = Tree(2)
child3 = Tree(3)
root.childrens = [child1, child2, child3]
child3.childrens = [Tree(6), Tree(7)]
child1.childrens = [Tree(4)]
child2.childrens = [Tree(8), Tree(9), Tree(10)]

BFS(root)