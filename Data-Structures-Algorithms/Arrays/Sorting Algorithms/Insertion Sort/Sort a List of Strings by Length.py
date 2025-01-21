"""
Sort a List of Strings by Length: 

Given a list of strings, use Insertion Sort to sort the strings based on their length. If two strings have the same length, maintain their order relative to each other (stable sort).

strings = ["word", "category", "at", "dog", "wonderful"]
# Sort these strings by their length using Insertion Sort.

"""
def sort_strings_by_length(strings):
    for i in range(len(strings)):
        current = strings[i]

        left = i - 1 
        while (left >= 0 and len(strings[left]) > len(current)) or (left >=0 and len(strings[left]) == len(current) and current < strings[left]):
            strings[left+1] = strings[left]
            left -= 1
        
        strings[left+1] = current
    return strings

strings = ["bod", "category", "cat", "dog", "wonderful"]
sort_strings_by_length(strings)