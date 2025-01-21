#Here is how you can create a Tree and add nodes to it, a node is composed by a data and its children refereces
"""In this example we intiilize the constructor, and create a method to add chilrens, this method is not necessary, it is useful when you don't know the number of nodes your tree is going to have, if your tree have a fixed size you do not need the method, when you do not have this method you can create the children specifying in the contructor, or just by manipulating the self.children array """

class Tree:
    def __init__(self,data):
        self.data = data #data in the node (root)
        self.childrens = [] #A list of children nodes

    def add_children(self, child_node):
        self.childrens.append(child_node) #Append the the list of children nodes of the root this child_node

root = Tree(4)
child1 = Tree(2)
child2 = Tree(3)
child3 = Tree(1)
Granchild = Tree(0)

root.add_children(child1)
root.add_children(child2)
root.add_children(child3)

child1.add_children(Granchild)

def printTree(root):
    print(root.data)
    for i in root.childrens:
        printTree(i)
printTree(root)
"""When you know the maximun number of node of the tree you can just specify the childrens in the constructor instead of having a list of children nodes, for example with a binary tree(top 2 nodes) you can just initilize the first and second childrens equal to None"""

class Binary_Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = Binary_Tree("Parent")
root.left = Binary_Tree('Left child')
root.right = Binary_Tree('Right child')
root.left.right = Binary_Tree('GrindChild')

def pre_order_traverse(root):
    if not root:
        return
    print(root.data)
    pre_order_traverse(root.left)
    pre_order_traverse(root.right)

pre_order_traverse(root)

def in_order_traverse(root):
    if not root:
        return
    
    in_order_traverse(root.left)
    print(root.data)
    in_order_traverse(root.right)

root = Binary_Tree('Root')
child1 = root.left=Binary_Tree('Child1')
child2 = root.right=Binary_Tree('Child2')
grandchild = child2.right=Binary_Tree('grandchild1')
grandchild2 = child2.left = Binary_Tree('grandchile2')

in_order_traverse(root)

"""Another common way is to use the constructor to specify the left an right childrens"""

class Binary_Tree:
    def __init__(self,data, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

"""Crete the tree: First way"""
root = Binary_Tree('Parent')
root.left = Binary_Tree('LeftChild')
root.right = Binary_Tree('RightChild')
root.left.left = Binary_Tree('LeftGrandChild')

"""Create the tree: Second way"""
root = Binary_Tree('Parent', 
                    left= Binary_Tree('LeftChild',
                                     left = 'LeftGrandChild'),
                    right = Binary_Tree('RightChild'))

def in_traverse(root):
    if not root:
        return
    in_traverse(root.left)
    print(root.data)
    in_traverse(root.right)

in_traverse(root)


""" You can also add childs by directly manipaleting the childrends list"""
class Tree:
    def __init__(self,data):
        self.data = data
        self.childrens = []

def traverse(root):
    if not root:
        return
    print(root.data)
    for child in root.childrens:
        traverse(child)

root = Tree(1)
child1 = Tree(4)
child2 = Tree(5)
root.childrens = [child1, child2]
child1.childrens = [Tree(2), Tree(3), Tree(1)]


traverse(root)
