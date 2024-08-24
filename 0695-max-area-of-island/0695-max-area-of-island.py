class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(mat,x,y,r,c):
            if (x<0 or x>=r or y<0 or y>=c or mat[x][y]!=1):
                return 0
            mat[x][y]=2
            return(1+dfs(mat,x+1,y,r,c)+
            dfs(mat,x-1,y,r,c)+
            dfs(mat,x,y+1,r,c)+
            dfs(mat,x,y-1,r,c))
        rows=len(grid)
        cols=len(grid[0])
        if rows==0:
            return 0
        count=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    count=max(count,dfs(grid,i,j,rows,cols))
        return count