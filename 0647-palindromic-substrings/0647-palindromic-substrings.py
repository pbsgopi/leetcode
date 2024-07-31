class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        def helper(i, j):
            nonlocal count
            while i >= 0 and j < n and s[i] == s[j]:
                count += 1
                i -= 1
                j += 1
        for i in range(n):
            helper(i, i)
            helper(i, i + 1)
        return count