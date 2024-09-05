class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        target = mean * (len(rolls)+n) - sum(rolls)
        if target < n or target > 6*n: return []
        a, b = divmod(target, n)
        return [a]*(n-b) + [a+1]*b