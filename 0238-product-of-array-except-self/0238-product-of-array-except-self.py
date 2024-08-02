class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans=[]
        n=len(nums)
        for i in range(n):
            mul=1
            for j in range(n):
                if j!=i:
                    mul*=nums[j]
            ans.append(mul)
        return ans