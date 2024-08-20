class Solution:
    def stoneGame(self, p: List[int]) -> bool:
        n=len(p)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=p[i]
        for j in range(1,n):
            for k in range(n-j):
                dp[k][k+j] = max(p[k]-dp[k+1][k+j],p[k+j]-dp[k][k+j-1])
        return dp[0][-1]>0