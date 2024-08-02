class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap={0:-1}
        ans,count=0,0
        for i,num in enumerate(nums):
            if num==1:
                count+=1
            else:
                count-=1
            if count in hashmap:
                ans=max(ans,i-hashmap[count])
            else:
                hashmap[count]=i
        return ans