class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m=len(haystack)
        n=len(needle)
        for i in range(m):
            if needle==haystack[i:i+n]:
                return i
        return -1