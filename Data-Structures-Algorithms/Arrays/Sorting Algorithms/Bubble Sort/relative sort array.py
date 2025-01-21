"""
Relative Sort Array

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
"""

#Create a hashtable tha count the number of occurrences of each element i arr1
#Iterate over arr2, for each element in arr2 add it to the result array as many times as is appears in arr1
#After procesing all elements in arr2, sort the remaining ones in arr2 in ascending order

def relative_sor(arr1, arr2):
    number_of_occurencers = {}
    result = []
    for i in arr1:
        if i in number_of_occurencers:
            number_of_occurencers[i] +=1
        else:
            number_of_occurencers[i] = 1
        
    for j in arr2:
        if j in number_of_occurencers:
            # result.extend([j]*number_of_occurencers[j])
            for k in range(number_of_occurencers[j]):
                result.append(j)
            del number_of_occurencers[j]
    
    remaining = []
    for k in number_of_occurencers:
        for i in range(number_of_occurencers[k]):
            remaining.append(k)

    for i in range(len(remaining)-1):
        swapped = False
        for j in range(len(remaining )- 1 - i):
            if remaining[j] > remaining[j+1]:
                remaining[j], remaining[j+1] = remaining[j+1], remaining[j]

    result.extend(remaining)

    return result
