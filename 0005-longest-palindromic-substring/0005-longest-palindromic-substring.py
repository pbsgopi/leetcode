class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ""
        def helper(i, j):
            nonlocal res
            while i >= 0 and j < n and s[i] == s[j]:
                if len(s[i: j + 1]) > len(res):
                    res = s[i: j + 1]
                i -= 1
                j += 1
        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return res