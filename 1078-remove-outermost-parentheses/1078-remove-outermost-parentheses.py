class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res=[]
        a=0
        for i in s:
            if i=='(' and a>0:
                res.append(i)
            if i==')' and a>1:
                res.append(i)
            if i=='(':
                a+=1
            else:
                a-=1
        return "".join(res)