"""
3. Level Order Traversal of a Tree
Problem Statement: Given a root of a tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example Usage:

Use the same TreeNode class where each node can have multiple children.
Implement a function level_order_traversal(root) that returns a list of lists, where each sublist contains the values of the nodes at that depth.

         1
        / \
       2   3
      / \   \
     4   5   6
        /
       7

output : [[1], [2, 3], [4, 5, 6], [7]]       
"""

class Tree:
    def __init__(self,data):
        self.data = data
        self.childrens = []
def level_order_traversal(root):
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        current_level = []
        level_size = len(queue)
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.data)

            for j in node.childrens:
                queue.append(j)

        result.append(current_level)
    return result

root = Tree(1)
child1 = Tree(2)
child2 = Tree(3)
child5 = Tree(6)
child6 = Tree(7)
child3 =Tree(4)
child4 = Tree(5)
root.childrens = [child1, child2]
child1.childrens = [child3, child4]
child2.childrens = [child5]
child4.childrens = [child6]

level_order_traversal(root)