"""
Sorting a List of Points by Distance:

Given a list of points in a 2D plane, sort them by their distance from the origin. You can calculate the distance of a point (x, y) from the origin using the formula 
raiz(x**2+y**2)

points = [(4, 4), (1, 1), (10, 2), (2, 3)]
# Sort the points by their distance from the origin using Bubble Sort.
"""
#Create a arabiel that calculates de distance of each element in the arr, we create that variable in the inner loop of the bubble sort algorithm
import math
def distanceOfPoints(arr):
    for left in range(len(arr)-1):
        swapped = False
        for right in range(len(arr)-1-left):
            distance1 = math.sqrt(((arr[right][0])**2 +(arr[right][1])**2))
            distance2 = math.sqrt(((arr[right+1][0])**2 +(arr[right+1][1])**2))
            if distance1 > distance2:
                arr[right], arr[right+1] = arr[right+1], arr[right]
        if not swapped:
            break
    return arr
points = [(4, 4), (1, 1), (10, 2), (2, 3)]
distanceOfPoints(points)

def distance(x,y):
    return math.sqrt(((x)**2 +(y)**2))
distance(4,4)
distance(2,3)
distance(10,2)