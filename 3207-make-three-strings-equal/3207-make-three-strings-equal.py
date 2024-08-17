class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        p, q, r = len(s1), len(s2), len(s3)
    
        for i in range(min(p, q, r)):
            if s1[i] == s2[i] == s3[i]:
                i += 1
            else:
                break
        return (p+q+r)-3*i if i != 0 else -1