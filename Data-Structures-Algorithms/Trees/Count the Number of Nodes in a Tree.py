"""
1. Count the Number of Nodes in a Tree
Problem Statement: Given a root of a tree (not necessarily a binary tree), count the total number of nodes in the tree.

Example Usage:

You can use the TreeNode class defined earlier, where each node can have multiple children stored in a list.
Implement a function count_nodes(root) that returns the total number of nodes in the tree.
"""

class TreeNode:
    def __init__(self,data):
        self.data = data
        self.childrens = []


#You have to have a count of one every time your are in the root of the tree, do this recursily
def count_nodes(root):
    if not root:
        return 0
    count = 1
    for child in root.childrens:
        count += count_nodes(child)

    return count

root = TreeNode(5)
child1 = TreeNode(3)
child2 = TreeNode(4)
child1.childrens = [TreeNode(1), TreeNode(9)]
root.childrens = [child1,child2]

count_nodes(root)

