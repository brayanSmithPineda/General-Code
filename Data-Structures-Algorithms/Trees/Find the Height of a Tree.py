"""
2. Find the Height of a Tree

Problem Statement: Given a root of a tree, find the height of the tree. The height of a tree is the number of edges on the longest downward path between the root and a leaf.

Example Usage:

Similar to the TreeNode class used earlier, but each node may contain multiple children.
Implement a function find_height(root) that returns the height of the tree.
"""
#We  go to the bottom of the tree by resursively call the function inside a foor loop, this is until we hit the base case
"""
def nameFunction(root):
    if not root.children:
        return 0

    for child in root.children:
        current_heigh = nameFunction(child)
"""
#When we hit the base case we need to decide what to do with the previous node that does not meet tha base condtion, in our problem what we need to do is to compare the result(current_height) we have with a variable that store the max_height and then return max_height + 1
"""
max_height = 0
for child in root.children:
    current_hegiht = nameFunction(child)
    max_heihgt = max(max_height, current_height)
return max_height + 1
"""

class Tree:
    def __init__(self,data):
        self.data = data
        self.childrens = []

    def add_child(self, child):
        self.childrens.append(child)

def heighTree(root):
    if not root.childrens:
        return 0
    
    max_heigh = 0
    for child in root.childrens: 
        current_height = heighTree(child)
        max_heigh = max(max_heigh, current_height)

    return max_heigh + 1
    
root = Tree(5)
child1 = Tree(4)
child2 = Tree(3)
root.add_child(child1)
root.add_child(child2)
child2.add_child(Tree(1))
grandchild =Tree(0)
child2.add_child(grandchild)
grandchild.add_child(Tree(6))

heighTree(root)

