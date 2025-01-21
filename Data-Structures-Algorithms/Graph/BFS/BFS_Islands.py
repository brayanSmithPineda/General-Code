"""
200. Number of Islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
"""

# key here is to identify that we need to perfom bfs on each element of the grid that is equal to one, to do that we just do an inner loop to go through every element in every row in every column, in each of those we perform bfs if its equal to 1 and its not already visited, keep in mind that we can always have a helper to perfom bfs in every element.

from collections import deque

def islindDFS(grid):
    if not grid:
        return -1
    
    number_islinds = 0
    number_rows, number_columns = len(grid), len(grid[0])
    visited = set()

    def bfs(grid, row, column):
        queue = deque([(row,column)])
        visited.add((row,column))
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        
        while queue:
            row, column = queue.popleft()
            for dr, dc in directions:
                new_row = row + dr
                new_col = column + dc
                if 0 <= new_row < number_rows and 0 <= new_col < number_columns and (new_row,new_col) not in visited and grid[new_row][new_col] == '1':
                    visited.add((new_row,new_col))
                    queue.append((new_row,new_col))

    for row in range(number_rows):
        for column in range(number_columns):
            if grid[row][column] == '1' and (row,column) not in visited:
                bfs(grid, row, column)
                number_islinds += 1

    return number_islinds

grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

islindDFS(grid)
# Example 1:


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]
islindDFS(grid)

grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

islindDFS(grid)