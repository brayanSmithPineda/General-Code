"""
Sorting Characters in a String: Given a string, sort the characters in the string in ascending order and return the sorted string. This will help you understand how Selection Sort can be applied to arrays of characters.
s = "selectionsort"
# Apply Selection Sort to arrange the characters in alphabetical order.
"""
def selectionSor(s):
    convert_string= list(s)

    for left in range(len(convert_string)):
        min_index = left
        for right in range(left+1,len(convert_string)):
            if convert_string[right] < convert_string[min_index]:
                min_index = right
            
        if min_index != left:
            convert_string[left], convert_string[min_index] = convert_string[min_index], convert_string[left]
    
    #Conver the list back to string
    string = ''.join(convert_string)
    return string
s = "selectionsort"
selectionSor(s)