class Solution:
    def findScore(self, nums: List[int]) -> int:
        n = len(nums)
        sorted_nums = sorted((num, idx) for idx, num in enumerate(nums))
        score = 0

        for num, idx in sorted_nums:
            if nums[idx] != -1:  # Process only if not already marked
                score += num
                nums[idx] = -1  # Mark current index
                if idx > 0:
                    nums[idx - 1] = -1  # Mark left neighbor
                if idx < n - 1:
                    nums[idx + 1] = -1  # Mark right neighbor

        return score
