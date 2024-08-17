
class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        l1 = len(s1) ; l2 = len(s2) ; l3 = len(s3)
        key_n = min([l1, l2, l3])
        
        key_num = key_n
        for i in range(key_n):
            if s1[i]!=s2[i] or s2[i]!=s3[i]:
                key_num = i
                break

        ans = l1+l2+l3-3*key_num if key_num != 0 else -1 
        
        return ans