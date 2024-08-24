class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row=len(grid)
        col=len(grid[0])
        visited=set()
        q=deque()
        def dfs(r,c):
            if (r<0 or r>=row or c<0 or c>=col or grid[r][c]==0 or (r,c) in visited):
                return
            visited.add((r,c))
            q.append([r,c])
        for i in range(row):
            for j in range(col):
                if grid[i][j]==2:
                    q.append([i,j])
                    visited.add((i,j))
        time=0
        while q:
            for i in range(len(q)):
                r,c=q.popleft()
                grid[r][c]=time
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
            time+=1
        for i in range(row):
            for j in range(col):
                if ((i,j) not in visited) and grid[i][j]==1:
                    return -1
        if time==0:
            return time
        return time-1