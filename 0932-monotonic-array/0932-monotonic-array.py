class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        nums_sorted=sorted(nums)
        return (nums==nums_sorted) or (nums[::-1]==nums_sorted)