class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowels = ['a','e','i','o','u']
        bitmask = [0] * 5
        firstoccurance = {0:-1}
        result = 0
        for i in range(len(s)):
            if s[i] in vowels:
                index = vowels.index(s[i])
                if bitmask[index] == 0:
                    bitmask[index] = 1
                else:
                    bitmask[index] = 0
            total = 0
            for j in range(5):
                total = total + bitmask[j]*(2**j)
            if total in firstoccurance:
                result = max(result, i-firstoccurance[total])
            else:
                firstoccurance[total] = i
        return result