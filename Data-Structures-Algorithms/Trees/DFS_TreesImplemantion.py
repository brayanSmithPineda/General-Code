#Iterative Way

#DFS traverse each branch as far as passible before moving to the next branch, is a vertical traversal.
#a difference between BFS and DFS is that in DFS to process the node horizontally that's why we used a queue because it allows us to process the first node that is added to the queue(FIFO), As in DFS what we want is to process the node vericatally we would use a Stack to process the last node added (LIFO)

class TreeNode:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

def dfs_iterative(root):
    if not root:
        return -1
    
    stack = [root]
    values = [] #This varaible will store the values we process from the DFS, this is just to show the order in which nodes are process with this algorithm

    while stack:
        node = stack.pop() #Here we have node we just pop, remember that with a stack the last element to be added is the one from be out,so that's why we use pop because it remove the element at the last position

        if node: #This condtion check is the node exist, that means it not None, this help us determine where the algorithm should stop and continue with the other brack
            values.append(node.data)
            stack.append(node.right) 
            stack.append(node.left)#It is a common practice to process firts the left branches, you know like going left to right, so that's way we append it at last because remember we're using LIFO approach
    
    return values

# Constructing a simple binary tree
#       1
#      / \
#     2   3
#    / \
#   4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

print(dfs_iterative(root))  # Output should be [1, 2, 4, 5, 3]


"""Pre-order traversal"""
def dfs_recursive(root):
    if not root:
        return
    print(root)
    dfs_recursive(root.left)
    dfs_recursive(root.right)

"""Returning the values"""

def dfs_values(root):
    if not root:
        return
    values = [root]
    values += dfs_values(root.left)
    values += dfs_values(root.right)

    return values 