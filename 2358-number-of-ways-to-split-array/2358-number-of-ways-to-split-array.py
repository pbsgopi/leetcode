class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        count=0
        total=sum(nums)
        target=0
        for i in range(len(nums)-1):
            target+=nums[i]
            if target>=total-target:
                count+=1
        return count