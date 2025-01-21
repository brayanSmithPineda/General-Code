def isValid(s):
    # Create a stack to keep track of opening brackets
    stack = []

    # Create a dictionary to map closing brackets to their corresponding opening brackets
    mapping = {")": "(", "}": "{", "]": "["}

    for i in s:
        if i in mapping:
            if stack and stack[-1] == mapping[i]:
                stack.pop()
            else:
                return "False"
        else:
            stack.append(i)

    return True if not stack else False
# Example usage:
example_string = "{[]}"
print(isValid(example_string))  # Output: True