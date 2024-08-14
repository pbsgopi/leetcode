class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        
        nums.sort()
        n = len(nums)
        left, right = 0, nums[-1] - nums[0]
        
        while left < right:
            mid = left + (right - left) // 2
            start = 0
            count = 0
            
            for i in range(n):
                while nums[i] - nums[start] > mid:
                    start += 1
                count += i - start
                
            if count < k:
                left = mid + 1
            else:
                right = mid
        
        return left