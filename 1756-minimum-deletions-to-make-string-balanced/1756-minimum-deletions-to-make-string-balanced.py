class Solution:
    def minimumDeletions(self, s: str) -> int:
        count=0
        ans=0
        for i in range(len(s)-1,-1,-1):
            if s[i]=='a':
                count+=1
            else:
                ans=min(ans+1,count)
        return ans