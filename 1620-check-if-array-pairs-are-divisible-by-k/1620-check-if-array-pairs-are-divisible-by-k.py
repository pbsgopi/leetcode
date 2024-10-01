class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:

        remainders = {}

        for num in arr:
            remainder = num % k
            remainders[remainder] = remainders.get(remainder, 0) + 1

        if remainders.get(0, 0) % 2 != 0:
            return False

        for i in range(1, k // 2 + 1):
            if remainders.get(i, 0) != remainders.get(k - i, 0):
                return False

        return True
        