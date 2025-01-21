# Understanding Linked Lists
# A linked list is a sequential collection of elements, but unlike arrays, these elements are not stored in contiguous memory locations. Each element in a linked list is a separate object called a 'node'. Each node consists of two parts:

# Data: The value stored in the node.
# Next: A reference (or link) to the next node in the sequence.

#Note: At the beggining of the linked list we have a reference that is pointing to the first element of the linked list, that reference is called the head, whith this we know whre our linked list start, is head in None that means the linked list is empty

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

node1.next = node2
node2.next = node3

linked_list = LinkedList()
linked_list.head = node1


#Operations in single linked-list
#--Travelsal
#---- Going through each element(node) of the linked-list
def traverseLinkedList(head):
    current_node = head #Left pointer at the haed that traverse the linked-list
    while current_node is not None:
        print(current_node.data)
        current_node = current_node.next
traverseLinkedList(node1)

def linkListToArray(head):
    list = []
    current_node = head #Left pointer at the haed that traverse the linked-list
    while current_node is not None:
        list.append(current_node.data)
        current_node = current_node.next
    return list
linkListToArray(node1)

#Insertion
#--- insert new nodes in a linked-list
## At the beggining

def insertAtBeggining(head, data):
    newNode = Node(data)
    newNode.next = head
    head = newNode
    return print(newNode.data, newNode.next.data)

insertAtBeggining(node1, 4)

## At the end

def insertAtEnd(head,data):
    newNode = Node(data)

    if head is None:
        head.next = newNode
        
    current = head
    while current.next is not None:
        current = current.next
    current.next = newNode

    return node3.data, newNode.data

insertAtEnd(node1, 500)

## Insertion: After a specific Node
def afterAtspecificNode(head,data,target):
    newNode = Node(data)
    current = head

    while current != None and current.data != target:
        current = current.next

    if current != None:
        newNode.next = current.next
        current.next = newNode
    

#Deletion
# --- Just like insertion, you can delete nodes from different positions:

#Delete the First Node (Head)
def deleteFirstNode(head):
    if head is not None:
        head = head.next
    return head
#Delete the last node
def deleteLastNode(head):

    if head is None:
        return None 

    current_pointer = head
    while current_pointer.next.next is not None:
        current_pointer = current_pointer.next
    current_pointer.next = None
    return head
    
# Delete a Specific Node: Find the node just before the node you want to delete and update its next pointer.
def deleteSpecificNode(head, data):
    if head == None:
        return None
    if head.data == data:
        return head.next
    current_node = head
    while current_node is not None:
        if current_node.next.data != data:
            current_node = current_node.next
            return head

        current_node.next = current_node.next.next
    return head

#Searching
#To find a particular element in a linked list, traverse the list and compare each node's data with the target value.

def findParticularElement(head, target):
    current = head
    while current is not None:
        if current.data == target:
            return current.data
        else:
            current = current.next
    return "Not Found"