MOD=10**9+7
class Solution:
    def countOfPairs(self, nums: List[int]) -> int:
        n = len(nums)    
        dp = [[0] * 1001 for _ in range(n + 1)]
        dp[n][:]=[1]*1001
        for i in range(n-1,-1,-1):
            diff=0
            if i:
                diff=max(0,nums[i]-nums[i-1])
            for j in range(1000,-1,-1):
                if j+1<=1000:
                    dp[i][j]=dp[i][j+1]
                if j+diff<=nums[i]:
                    dp[i][j]=(dp[i][j]+dp[i+1][j+diff])%MOD
        return dp[0][0]