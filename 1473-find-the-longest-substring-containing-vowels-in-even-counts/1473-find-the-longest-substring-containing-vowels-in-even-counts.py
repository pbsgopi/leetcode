class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowel = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}
        memo = {0: -1}
        mask = 0 
        result = 0
        n = len(s)
        for i in range(n):            
            c = s[i]
            if c in vowel:
                mask = mask ^ vowel[c]
            if mask not in memo:
                memo[mask] = i
            else:
                result = max(result, i - memo[mask])
        return result