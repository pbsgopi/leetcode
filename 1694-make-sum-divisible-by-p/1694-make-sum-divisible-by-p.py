class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        remainder = sum(nums) % p
        if remainder == 0: return 0

        cursum = 0
        remToInd = { 0 : -1 }
        res = len(nums)

        for i, n in enumerate(nums):
            cursum = (cursum + n) % p
            prefix = (cursum - remainder + p) % p
            if prefix in remToInd:
                sublen = i - remToInd[prefix]
                res = min(res, sublen)
            remToInd[cursum] = i
        
        if res == len(nums): return -1
        return res