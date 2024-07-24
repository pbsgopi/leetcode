class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        m=len(a)
        n=len(b)
        count=1
        repeat=n//m
        while count<=repeat+2:
            if b in count*a:
                return count
            else:
                count+=1
        return -1