class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(mat,x,y,r,c):
            if (x<0 or x>=r or y<0 or y>=c or mat[x][y]!='1'):
                return
            mat[x][y]='2'
            dfs(mat,x+1,y,r,c)
            dfs(mat,x-1,y,r,c)
            dfs(mat,x,y+1,r,c)
            dfs(mat,x,y-1,r,c)
        rows=len(grid)
        cols=len(grid[0])
        if rows==0:
            return 0
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]=='1':
                    dfs(grid,i,j,rows,cols)
                    count+=1
        return count