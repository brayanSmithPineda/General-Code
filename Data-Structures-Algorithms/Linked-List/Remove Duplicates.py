# 83. Remove Duplicates from Sorted List

# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

# Input: head = [1,1,2]
# Output: [1,2]

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, head) -> None:
        self.head = head

#Check is the node.data at position 0 is equal to the one at position 1, if its unique move to the current pointer, if its equal then change the pointer to the next node
        
def removeDuplicates(head):
    current = head
    traverse_pointer = head
    while current and current.next :
        if current.data != current.next.data:
            current = current.next
        elif current.data == current.next.data:
            current.next = current.nex.next
    return head