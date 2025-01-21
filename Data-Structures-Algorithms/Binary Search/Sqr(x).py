# Sqrt(x)

# Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

# You must not use any built-in exponent function or operator.

# For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
# Example 1:

# Input: x = 4
# Output: 2
# Explanation: The square root of 4 is 2, so we return 2.

def sqr(x):
    left, right = 0, x
    while left <= right:
        middle = left + (right-left)//2
        if middle**2 > x:
            right = middle -1
        elif middle**2 < x:
            left = middle +1
            res = middle
        else:
            return middle
    return res