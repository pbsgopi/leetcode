class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = 0
        for num in nums:
            total += num
        
        if total < target:
            return 0
        
        target = (total - target)
        
        if target % 2 == 1:
            return 0
        
        target = target // 2

        dp = [0] * (target + 1)
        dp[0] = 1

        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] + dp[i - num]
        
        return dp[target]