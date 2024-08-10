class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n, regions = len(grid), 0
        g = [[0] * n * 3 for _ in range(n*3)]
        
        def dfs(i, j):
            if 0 <= min(i, j) and max(i, j) < n*3 and g[i][j] == 0:
                g[i][j] = 1
                return 1 + dfs(i+1, j) + dfs(i-1, j) + dfs(i, j+1) + dfs(i, j-1)
            return 0
        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == '/':
                    g[i*3+2][j*3] = g[i*3+1][j*3+1] = g[i*3][j*3+2] = 1
                elif grid[i][j] == '\\':
                    g[i*3][j*3] = g[i*3+1][j*3+1] = g[i*3+2][j*3+2] = 1
        
        for i in range(3*n):
            for j in range(3*n):
                regions += 1 if dfs(i, j) > 0 else 0
        return regions