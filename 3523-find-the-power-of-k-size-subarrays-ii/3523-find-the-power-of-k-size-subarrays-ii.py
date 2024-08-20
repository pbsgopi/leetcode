class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        res = []       
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1] + 1:
                cons += 1
            else:
                cons = 1
            if i + 1 >= k:
                res.append(nums[i] if cons >= k else -1)
        return res