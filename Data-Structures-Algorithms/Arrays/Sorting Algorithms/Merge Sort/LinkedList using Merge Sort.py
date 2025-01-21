"""
Sort a LinkedList using Merge Sort
Implement the Merge Sort algorithm to sort a singly linked list. You'll need to modify the merge sort to work on linked list nodes instead of array indices, which will test your understanding of pointers and node manipulation.

Input: 4 -> 2 -> 1 -> 3
Output: 1 -> 2 -> 3 -> 4
"""
#Class to define the Nodes
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#Return and print the linked list
def print_result(head):
    current = head
    while current:
        print(current.data, end="->")
        current = current.next
    print('None')

#Main Function
def merge_sort(head):
    if not head or not head.next:
        return head
    else: 
        middle_node = middle_linkedList(head)
        middle_node_next = middle_node.next
        middle_node.next = None

        left = merge_sort(head)
        right = merge_sort(middle_node_next)

        return merge(left,right)
    
def middle_linkedList(head):
    slow, fast = head, head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def merge(left, right):
    dummy_head = Node(-1)
    tail = dummy_head
    while left and right:
        if left.data <= right.data:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    
    if left:
        tail.next = left
    if right:
        tail.next = right
    
    return dummy_head.next

head = Node(4)
second = Node(2)
third = Node(1)
fourth = Node(3)

head.next = second
second.next = third
third.next = fourth

res_head = merge_sort(head)
print_result(res_head)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def printresult(head):
    current = head
    while current:
        print(current.data, end="->")
        current = current.next
    print("None")

def merger_sort2(head):
    if not head or not head.next:
        return head
    else:
        middle = middle_linkedList2(head)
        middle_point_head = middle.next
        middle.next = None

        left = merger_sort2(head)
        right = merger_sort2(middle_point_head)

        return merge2(left, right)


def middle_linkedList2(head):
    slow, fast = head, head.next
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    
    return slow

def merge2(left, right):
    dummy_node = Node(-1)
    tail = dummy_node
    left_current = left
    right_current = right
    while left_current and right_current:
        if left_current.data <= right_current.data:
            tail.next = left_current
            left_current = left_current.next
        else:
            tail.next = right_current
            right_current = right_current.next  
        tail = tail.next

    if left_current:
        tail.next = left_current
    if right_current:
        tail.next = right_current
    
    return dummy_node.next

head = Node(4)
second = Node(2)
third = Node(1)
fourth = Node(3)

head.next = second
second.next = third
third.next = fourth

res_head = merger_sort2(head)
printresult(res_head)