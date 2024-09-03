class Solution:
    def getLucky(self, s: str, k: int) -> int:
        res =""

        for i in range(len(s)):
            res+=str((ord(s[i])-96))
        
        for i in range(k):
            s=0
            for j in range(len(res)):
                s+=int(res[j])
            res = str(s)

        return int(s)