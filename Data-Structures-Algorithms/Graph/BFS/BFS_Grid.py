"""
Example: BFS on a Grid
Let's say we have a grid where 1 represents a wall and 0 represents an open path. We want to find the shortest path from the top-left corner to the bottom-right corner, moving only up, down, left, or right.
"""

from collections import deque

def bfs(grid):
    if not grid:
        return -1  # or some indication that the path is impossible
    
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    queue = deque([((0, 0), 0)])  # ((row, col), distance) start the traversla from the top-left corner, the next element 0 represent the distance from the starting point since we are at the starting point the distance is cero. Note: we always sorround the elemnt in brackets
    visited = set((0, 0)) # Here as we initilize the queue with the starting top-left vertix we mark it as visited, as we are in a grid we have to save the index of the vertix
    
    while queue:
        (row, col)  , dist = queue.popleft() #queue.popleft() remove the first element of the queue and returns it, so lets say the first element is ((1,2),2) so thats the value queue.popleft is retuning, then we unpuck those two values in the set and assing them to the varaibles (row,col), dist so (row,col) = (1,2) and dist = 2
        
        # Check if we've reached the destination
        if row == rows - 1 and col == cols - 1: #Here our destination is the bottom-right corner thats way row, col varaibles that store our current poisition should be equal to rows - 1 (len(grid)) and cols -1 (len(grid[0]))
            return dist #If we reach the destination we return the dist from the starting point to the end point, this is what the problem is telling us to return
        
        #If we haven't reach the destination then we explore neighbors
        for dr, dc in directions: #dr and dc is going to unpack each tuple element of the directions array, that way we can go up,down,left and right
            new_row, new_col = row + dr, col + dc #here the new neighbor is not going to be dr or dc, remember that this element just dictates we are we going to move, the real neigbors are going to be the sum of row + dr and col + dc (row, col we are righ plus the direction)
            if 0 <= new_row < rows and 0 <= new_col < cols and grid[new_row][new_col] == 0 and (new_row, new_col) not in visited: #here we check 4 condtion, first that new row and new column are withind bound, second that the vertix at those indexes is  eqaul to cero beacause the problem state that this are the only viable path if we encounter another value that means we can not go in that direction beacause is block, and the we check is that vertix is in the visited so if it is we do not need to explore it again. 
                visited.add((new_row, new_col)) # we add the new row, col in the visited set
                queue.append(((new_row, new_col), dist + 1)) # we add them to the queue as well to explore them, we also increment the dist by one
    
    return -1  # Path not found

# we are given a grid and we need to find the shorest path from the top-left corner to the bottom right corner, only cero are a valid path.

# we need to check is the grid that we are given is a valid grid, that means in not none

#Then we set the queue, visited and directions variables, with these we can perfom our algorithm, queue is going to track the nodes that we need to process, visited track the nodes that we already processed, and directions is going to have the changes in row,col so we can move up,righ,down and left to see for neighbor
#then we loop trough while the queue is not empy
# in that case we pop the first element of the queue and save in a variable, here we need to unpack the (row,col), dist
# afte we pop it we use the upacked variables to see if the row, col is already at the destination vertix, if that is the case we return the dist
# else we just process the neighbors
# in case we do not find any path after the while loop we just return -1

def bfs_practice(grid):
    if not grid:
        return -1
    rows, cols = len(grid), len(grid[0]) # this is later use to identify is we are out of bound and to indintify the buttom-righ corner
    queue = deque([((0, 0), 0)]) # we initlize the queue at the top-left corner vertix and the initlize distance from the destination right now as we are at the beggining node the the distance is just cero
    visited = set ((0,0)) # we intilize the set with the top-left corner vertix
    directions = [(0,1), (0,-1), (1,0), (-1,0)] #right,left, down,up
    while queue:
        (row,col), dist = queue.popleft()

        if row == rows - 1 and col == cols - 1: #This means we already reach the bottom-left coner vertix
            return dist # in case the we reach the goal we just return the distance
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0<=new_row<=rows-1 and 0<=new_col<=cols-1 and (new_row,new_col) not in visited and grid[new_row][new_col] == 0:
                visited.add((new_row,new_col)) # we add the nodes to the visit one
                queue.append(((new_row,new_col),dist+1)) # we append to the queue thw new nodes and the new distance

    return -1 

grid1 = [
[0, 1],
[1, 0]
]

bfs_practice(grid1)

grid2 = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
bfs_practice(grid2)

grid3 = [
    [0, 1, 0],
    [0, 0, 0],
    [1, 0, 0]
]
bfs_practice(grid3)

grid4 = [
    [0, 0, 0, 0],
    [0, 1, 1, 0],
    [0, 1, 0, 0],
    [0, 0, 0, 0]
]

bfs_practice(grid4)