"""
Sort to linked list in place
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def merge_linked_list(head1,head2):
    dummy_node = Node(-1)
    prev_pointer = dummy_node
    while head1 and head2:
        if head1.data <= head2.data:
            prev_pointer.next = head1
            head1 = head1.next
        else:
            prev_pointer.next = head2
            head2 = head2.next
        prev_pointer = prev_pointer.next

    if head1:
        prev_pointer.next = head1
    else:
        prev_pointer.next = head2

    return dummy_node.next


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4

def print_linkedList(head):
    current = head
    while current:
        print(current.data, end="->")
        current = current.next
    print("None")
print_linkedList(node1)