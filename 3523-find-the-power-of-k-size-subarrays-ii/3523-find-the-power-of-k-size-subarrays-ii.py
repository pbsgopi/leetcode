from collections import deque
from typing import List

class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        results = [-1] * (n - k + 1)
        dp = [0] * n
        deq = deque()
        
        for i in range(1, n):
            if nums[i] - nums[i - 1] == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = 0

        for i in range(n):
            while deq and deq[0] < i - k + 1:
                deq.popleft()
                
            while deq and nums[deq[-1]] <= nums[i]:
                deq.pop()
                
            deq.append(i)
            
            if i >= k - 1:
                if dp[i] >= k - 1:
                    results[i - k + 1] = nums[deq[0]]
        
        return results
