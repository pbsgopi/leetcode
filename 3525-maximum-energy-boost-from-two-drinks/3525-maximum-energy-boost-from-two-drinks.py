class Solution:
    def maxEnergyBoost(self, eA: List[int], eB: List[int]) -> int:
        n=len(eA)
        dpA=[0]*(n)
        dpB=[0]*(n)
        for i in range(n):
            dpA[i] = max(dpA[i - 1], dpB[i - 2]) + eA[i]
            dpB[i] = max(dpB[i - 1], dpA[i - 2]) + eB[i]
        return max(dpA[n-1],dpB[n-1])