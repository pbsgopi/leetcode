class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        mod=10**9+7
        res=[]
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                res.append(s)
        #ans=sorted(res)
        res.sort()
        return sum(res[left-1:right])%mod