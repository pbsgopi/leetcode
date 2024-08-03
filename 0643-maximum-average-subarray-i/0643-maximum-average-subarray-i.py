class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxsum=cursum=sum(nums[:k])
        for i in range(k,len(nums)):
            cursum+=nums[i]-nums[i-k]
            maxsum=max(maxsum,cursum)
        return maxsum/k