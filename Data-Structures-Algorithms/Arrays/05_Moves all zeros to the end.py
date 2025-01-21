# Move all Zeros to the End of the Array:

# Given an array, write a function to move all 0's to the end of it while maintaining
# the relative order of the non-zero elements.



# loop through the array and check if the number is grater than cero
# if so loo trhough the array again
# if so then swap it

def movesZeros (arr):
    i= 0
    for j in range(len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i+=1
    return arr
arr = [1,0,2,3,0,0,4,0,0,0,0,5,0,6]
movesZeros(arr)



