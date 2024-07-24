class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        a=0
        b=0
        for i in s:
            if i=="(":
                a+=1
            elif i==")":
                if a>0:
                    a-=1
                else:
                    b+=1
        return a+b