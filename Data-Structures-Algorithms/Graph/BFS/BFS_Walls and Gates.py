"""
Walls and Gates Problem Statement:
You are given a m x n 2D grid initialized with three types of values:

-1: A wall or an obstacle.
0: A gate.
INF: Infinity means an empty room. We use the value 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, leave the room as INF.

Example 1:
Input:

Copy code
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
Output:

Copy code
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
Explanation: The 2D grid is as follows:

Top-left INF is 3 steps away from the nearest gate at (0, 2).
The INF at (1, 0) is 2 steps away from the nearest gate.
The bottom-right INF is 4 steps away from the nearest gate at (3, 0).
"""

#We are going to loop through every row and every column of the grid
#an important key here is that we are going to perform BFS from the gates similtanously, this is really important beacause if we start from the empty room our time complexity will be significally higher beacause we are going to traver each element more that one time, and we do the BFS simoultaniouly because if we jus do with one at a time we are going to fill all the empty room with a value just taking into consideration one gate.

from collections import deque

def walls_gates(grid):
    if not grid:
        return -1
    
    rows, columns = len(grid), len(grid[0])
    visited = set()
    queue = deque()
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    
    for row in rows:
        for column in columns:
            if grid[row][column] == 0:
                queue.append([((row,column),0)])

    while queue:
        (row, column), dist = queue.popleft()
        visited.add((row,column))
        
        if grid[row][column] == float('inf'):
            grid[row][column] = dist + 1

        for dr, dc in directions:
            new_row = row + dr
            new_colum = column + dc
            if  0<= new_row <rows and 0<=new_colum<columns and (new_row, new_colum) not in visited and grid[new_row][new_colum] == float('inf'):
                visited.add((new_row,new_colum))
                queue.append(((new_row,new_colum), dist +1))

    

grid1 = [
    [0, -1, float('inf')],
    [float('inf'), float('inf'), -1],
    [float('inf'), float('inf'), 0]
]
walls_gates(grid1)





#The key to this is problem is to know that a more efficient way to perform BFS is staring from gate nodes, that we could replace any distance of the empty room nodes
#To start from the gates you need to initilize the queue with the gates, to find the gates you perfom a nested loop and append to queue those values that are eqaul to the gate grid[row][column] == 0.
#Then you also have to notice that you first traver a gate and update all the empty room from that first gate, but probably if you start bfs from another gate your going to find distance for some rooms that are lower than the distance you privously calculated from the first gate, so you have to make sure to update those empty rooms in case the distance is lower


from collections import deque

def walls_and_gates(grid):
    if not grid:
        return
    num_rows, num_cols = len(grid), len(grid[0])
    queue = deque()

    # Step 1: Initialize the queue with all gates
    for row in range(num_rows):
        for col in range(num_cols):
            if grid[row][col] == 0:
                queue.append((row, col, 0))  # (row, col, distance)

    # Step 2: Perform BFS from each gate
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while queue:
        row, col, dist = queue.popleft()
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            # Update distance if the next cell is an empty room and the new distance is shorter
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] > dist + 1: #The key of the problem is in this condition grid[new_row][new_col] > dist +1, this means we only going to replace the value of the grid at that position if the new distance is lower than the current one, that way when you finish to traver an entire gate probably all the rooms will be with distances so we only going to replace distance in case we find a lower one. A really important tricky condition here is that we also have to just analyze only the neighbors that are equal to inf (all less -1), this condition is undirected cover by the same condition we just talk about, as -1 are the walls so -1 is never going to be greater than new distance so is never going to be added to the queue and therefore we are not going to perform bfs on those neigbors, this condition also make sure that we do not visit the node again, it is like a visited set, bacause we only traverse that node if the new distancre is strictly grater than the current one and that never going to happend if we already traverse that node because is going to have the same distance so we never enter the loop, Once an INF cell is updated with a numerical distance, it's no longer considered for updating again because any subsequent distance calculated would be equal or greater due to the nature of BFS
                grid[new_row][new_col] = dist + 1
                queue.append((new_row, new_col, dist + 1))

def wallsGatesTwo(grid):
    if not grid:
        return 'Not a valid grid'
    
    rows, columns = len(grid), len(grid[0])
    #Append to the queue the gates
    queue = deque()
    for row in range(rows):
        for col in range(columns):
            if grid[row][col] == 0:
                queue.append((row,col,0)) #row, column, distance from gate
    
    #visited = set() we could initlize a visited set to keep track of nodes we already visit, but we can do that by directyl modifying the grid and set a condtion to not process those nodes, grid[new_row][new_col] > dist + 1,once an INF cell is updated with a numerical distance, it's no longer considered for updating again because any subsequent distance calculated would be equal or greater due to the nature of BFS
    #perfom bfs
    directions = [(0,1), (0,-1), (1,0), (-1,0)]
    while queue:
        row, col, distance = queue.popleft()
        for dr, dc in directions:
            new_row = row + dr
            new_col = col + dc
            if 0<=new_row<rows and 0<=new_col<columns and grid[new_row][new_col] > distance + 1:
                queue.append((new_row,new_col,distance + 1))
                grid[new_row][new_col] = distance + 1
    
    return grid

grid1 = [
    [float('inf'), -1, 0, float('inf')],
    [float('inf'), float('inf'), float('inf'), -1],
    [float('inf'), -1, float('inf'), -1],
    [0, -1, float('inf'), float('inf')],
]

wallsGatesTwo(grid1)