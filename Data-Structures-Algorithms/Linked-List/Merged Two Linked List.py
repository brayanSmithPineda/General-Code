# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

#We going to compare each node of each linked list
#
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None

def mergeTwoLists(list1, list2):
    dummy = Node(-1)
    pointer = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            dummy.next = list1
            list1 = list1.next
        elif list2.data > list2.data:
            dummy.next = list2
            list2 = list2.next
        pointer = pointer.next

    pointer.next = list1 or list2
    return dummy.next


def sumLinkedList(head):
    sum = 0
    current = head
    while current is not None:
        sum += head.data
        current = current.next
    return sum

def findTarget(head, target):
    current = head
    while current is not None:
        if current.data == target:
            return True
        current = current.next
    return "Not Found"

def findByIndex(head, index):
    index_value = 0
    current = head
    while current is not None:
        if index_value == index:
            return current.data
        
        index_value += 1
        current = current.head

    return "Not Found"

def reverse(head):
    previous = None
    current = head
    while current is not None:
        next = current.next
        current.next = previous
        previous = current
        current = next
        

    return previous

def zipperList(head1,head2):
    tail = head1
    current1 = head1
    current2 = head2
    count = 0
    while current1 and current2:
        if count%2 == 0:
            tail.next = current2.next
            current2 = current2.next
        elif count%2 > 0:
            tail.next = current1.next
            current1 = current1.next
        count += 1
        tail = tail.next
    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2
        
    return tail