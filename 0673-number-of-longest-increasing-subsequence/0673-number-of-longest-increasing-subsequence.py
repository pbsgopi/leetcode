class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[1]*n
        count=[1]*n
        maxi=1
        for i in range(n):
            for j in range(i):
                if nums[i]>nums[j] and dp[i]<1+dp[j]:
                    dp[i]=1+dp[j]
                    count[i]=count[j]
                elif nums[i]>nums[j] and dp[i]==1+dp[j]:
                    count[i]+=count[j]
            maxi=max(maxi,dp[i])
        num=0
        for i in range(n):
            if dp[i]==maxi:
                num+=count[i]
        return num