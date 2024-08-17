class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        res = []
        
        for i in range(n - k + 1):
            subarray = nums[i:i + k]
            if subarray == list(range(min(subarray), min(subarray) + k)):
                res.append(max(subarray))
            else:
                res.append(-1)
        return res