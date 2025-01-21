"""
20. Valid Parentheses
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true

Input: s = "{[()]}"
Output: true
"""
#Approach
#1--every time you find a open just continue traversing the string
#2--Once you find a closing bracket you have to check if the previous one was the same open bracket, if it is the just delete that pair which is correct, if it is not then return False, continue this loop

#This was indeed in the right track, but you did not apply the right implementation in code, here is how you can identify we need a stack:

#As we say need to check if each opening bracket has a corresponding closing braket and then remove them, we just traverse the string until we find and closing bracket and compare it with the last seen opening bracket, if they match each other we remove them, and continue with the loop

#The key there is that we need to compare the closing bracket with the LAST seen bracket, here is how we can know we need to use a stack, the LIFO property of a stack makes them ideal when you when you need to traverse things or check for matching pairs that are nested. Parenthesis need to be closed in the reverse order they are opened when they are netsted, {([])}, in this example { is opend at first and its closing one is at the last position. When dealing with nested structures or sequences where elements must balance each other, stacks help manage these pairs effeciently. When you have problems that involves nested or recursives structures where you need to return to an early state, return the recent data, or baling pairs, stack is the right path 

def valid_parethesis(string):
    hashmap = {')':'(', '}':'{', ']':'['}
    stack = []

    for parathesis in string:
        if parathesis not in hashmap:#We append  the opening bracket to the stack
            stack.append(parathesis)
        else: #This means we encounter a closing bracket
            if stack and stack[-1] == hashmap[parathesis]: #if stack is not empty and the last seen opening parenthesis is equal to its corresponding parenthesis, then we know is a valid pair and we just removit
                stack.pop()
            else: #if the stack is empty or the pair is not valid one, we just return Flase
                return False
    if not stack:
        return True
    
s = "{[()}"
valid_parethesis(s)