from typing import List

class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(mat, x, y, r, c):
            if x < 0 or x >= r or y < 0 or y >= c or mat[x][y] != 1:
                return
            mat[x][y] = 0
            dfs(mat, x + 1, y, r, c)
            dfs(mat, x - 1, y, r, c)
            dfs(mat, x, y + 1, r, c)
            dfs(mat, x, y - 1, r, c)

        rows = len(grid)
        cols = len(grid[0])
        if rows == 0:
            return 0
        
        for i in range(rows):
            for j in [0, cols-1]:
                if grid[i][j] == 1:
                    dfs(grid, i, j, rows, cols)
        for j in range(cols):
            for i in [0, rows-1]:
                if grid[i][j] == 1:
                    dfs(grid, i, j, rows, cols)
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
        
        return count
