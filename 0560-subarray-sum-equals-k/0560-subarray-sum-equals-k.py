class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_map = {}
        prefix_map[0] = 1
        prefix_sum = 0
        res = 0
        for num in nums:
            prefix_sum += num
            if (prefix_sum - k) in prefix_map:
                res += prefix_map[prefix_sum - k] 
            prefix_map[prefix_sum] = 1 + prefix_map.get(prefix_sum, 0)
        return res