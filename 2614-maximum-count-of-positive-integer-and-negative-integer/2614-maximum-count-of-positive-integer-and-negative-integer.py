class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        l = bisect_left(nums, 0)
        r = bisect_right(nums, 0)
        
        n = len(nums)
        return max(l, n-r)