"""
Input: "the simple engineer"
output: "reenigne elpmis eht"
"""

def reverse_string_recursively(string):
    #base case: when can i no longer continue?, if i would just pass it an input, what is the smallest input that i can pass to this function where i need inmmediatly return. Empty string.
    if string == "":
        return ""

    #what is the smallest amount of work that i could do in each iteration?, how do i even get to the point of the base case, how do i get to the point where the string is empty?, this section is divided in two parts the recursive call that shrink the input and the smallest unit of work to contribuite

    return reverse_string_recursively(string[1:]) + string[0]

string = "the simple engineer"
reverse_string_recursively(string)