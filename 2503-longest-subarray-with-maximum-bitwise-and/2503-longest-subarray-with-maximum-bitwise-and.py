class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxAnd = max(nums)
        length = 0
        i = 0
        while i < len(nums):
            lo = i
            while i < len(nums) and nums[i] == maxAnd:
                i += 1
            length = max(length, i-lo)
            i += 1
        return length