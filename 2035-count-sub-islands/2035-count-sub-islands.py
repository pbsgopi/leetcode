class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m=len(grid1)
        n=len(grid1[0])
        visited=set()
        def dfs(r,c):
            if (r<0 or r>=m or c<0 or c>=n or grid2[r][c]==0 or ((r,c) in visited)):
                return True
            visited.add((r,c))
            res=True
            if grid1[r][c]==0:
                res=False
            
            res=dfs(r+1,c) and res
            res=dfs(r-1,c) and res
            res=dfs(r,c+1) and res
            res=-dfs(r,c-1) and res
            return res 
        count=0
        for i in range(m):
            for j in range(n):
                if grid2[i][j] and (i,j) not in visited and dfs(i,j):
                    count+=1
        return count