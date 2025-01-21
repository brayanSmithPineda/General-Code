"""
Sort a List of Products

Suppose you have a list of products, where each product is represented by a tuple containing the product name and its price. Your task is to sort the list based on the price in ascending order. If two products have the same price, they should be sorted by their names in alphabetical order.

products = [("apple", 50), ("banana", 10), ("orange", 20), ("mango", 20)]
# Apply Bubble Sort to sort the products first by price, then by name if the prices are equal.
"""
def sort_producst(arr):
    for left in range(len(arr)-1):
        swapped = False
        for right in range(len(arr)-1-left):
            if arr[right][1] > arr[right+1][1]:
                arr[right], arr[right+1] = arr[right+1], arr[right]
                swapped =True
            elif arr[right][1] == arr[right+1][1] and arr[right][0] > arr[right+1][0]:
                arr[right], arr[right+1] = arr[right+1], arr[right]
                swapped =True
        if swapped == False:
            break
    return arr

products = [("apple", 50), ("banana", 10), ("orange", 20), ("mango", 20),("coconut", 20)]
sort_producst(products)