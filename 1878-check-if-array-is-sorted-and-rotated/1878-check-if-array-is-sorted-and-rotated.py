class Solution:
    def check(self, nums: List[int]) -> bool:
        n= len(nums)
        sorted_nums=sorted(nums)
        for i in range(n):
            if nums[i:]+nums[:i]==sorted_nums:
                return True
        return False