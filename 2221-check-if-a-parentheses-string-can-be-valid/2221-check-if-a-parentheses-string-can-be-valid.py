class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        opened=0
        if len(s)%2!=0:
            return False
        for i in range(len(s)):
            if s[i]=='(' or locked[i]=='0':
                opened+=1
            else:   
                opened-=1
            if opened<0:
                return False
        closed=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')' or locked[i]=='0':
                closed+=1
            else:
                closed-=1
            if closed<0:
                return False
        return True
