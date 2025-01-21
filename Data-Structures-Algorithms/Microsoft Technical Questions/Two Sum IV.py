"""
653. Two Sum IV - Input is a BST

Given the root of a binary search tree and an integer k, return true if there exist two elements in the BST such that their sum is equal to k, or false otherwise.

Input: root = [5,3,6,2,4,null,7], k = 9
Output: true

Input: root = [5,3,6,2,4,null,7], k = 28
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 104].
-104 <= Node.val <= 104
root is guaranteed to be a valid binary search tree.
-105 <= k <= 105
"""

#Traverse the tree
#we could also see if the complement is a hashmap x = target - node, if not in a hashmap then we append the node with the node value as its key and the number of times as the value
from collections import deque

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

def binary_search_tree(root, target):
    if not root:
        return False 
    
    hashmap = {}
    queue = deque([root])
    while queue:
        node = queue.popleft()
        x = target - node.data 

        if x not in hashmap:
            hashmap[node.data] = 1
        else:
            return True, [x, node.data]
        
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return False

# Constructing the binary search tree
#       5
#      / \
#     3   6
#    / \   \
#   2   4   7

root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(7)

# Now let's test your binary_search_tree function

# Test case 1: Should return True, [2, 5]
print(binary_search_tree(root, 7))

# Test case 2: Should return True, [3, 4]
print(binary_search_tree(root, 7))

# Test case 3: Should return False
print(binary_search_tree(root, 10))

# Test case 4: Should return True, [2, 6]
print(binary_search_tree(root, 8))

# Test case 5: Edge case with only one element, should return False
single_node_tree = TreeNode(1)
print(binary_search_tree(single_node_tree, 2))


def dfs_recursive(root, target):
    if not root:
        return
    hashmap = {}
    complement = target - root
    if complement not in hashmap:
        hashmap[root] = 1
    else:
        return True
    dfs_recursive(root.left)
    dfs_recursive(root.right)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findTarget(root, k):
    def dfs(node, k, seen):
        if not node:
            return False
        if k - node.val in seen:
            return True
        seen.add(node.val)
        return dfs(node.left, k, seen) or dfs(node.right, k, seen) #The or operator is crucial here because it allows us to stop the search as soon as we find a valid pair in either the left or right subtree., that's why we use a return statement to stop the execuation as soon of one part is True
    
    return dfs(root, k, set()) #A set is more appropiate to use because we just need to return True or False if a pair has been seen we do not need to store any extra information
