class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if n & k != k: return -1
        return n.bit_count() - k.bit_count()