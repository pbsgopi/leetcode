class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        res=[]
        j=0
        for i in range(len(nums)):
            if i+1==len(nums) or (nums[i]+1)!=(nums[i+1]):
                if j==i:
                    res.append(str(nums[i]))
                else:
                    res.append(str(nums[j])+'->'+str(nums[i]))
                j=i+1
        return res