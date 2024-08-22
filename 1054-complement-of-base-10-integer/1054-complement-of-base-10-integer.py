class Solution:
    def bitwiseComplement(self, n: int) -> int:
        n=bin(n)
        s=str(n)
        num=s[1:]
        res=''
        for i in num:
            if i=='1':
                res+='0'
            else:
                res+='1'
        ans=res[1:]
        count=0
        for i in range(len(ans)):
            count+=int(ans[i])*(2**(len(ans)-i-1))
        return count