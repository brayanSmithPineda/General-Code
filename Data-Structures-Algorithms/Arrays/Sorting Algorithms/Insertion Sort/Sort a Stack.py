"""
Sort a Stack: 

Given a stack (you can use a list as a stack in Python), write a function that sorts the stack using Insertion Sort principles. You should only use standard stack operations: push, pop, peek, and isEmpty.

stack = [34, 3, 31, 98, 92, 23]
# Define a function to sort this stack using principles of Insertion Sort.

"""

def sort_stack(stack):
    temp_stack = []
    while stack:
        current = stack.pop()
        while temp_stack and temp_stack[-1] > current:
            stack.append(temp_stack.pop())

        temp_stack.append(current)

    return temp_stack

stack = [34, 3, 31, 98, 92, 23]
sort_stack(stack)




arr = [1,2,4]
arr.pop()