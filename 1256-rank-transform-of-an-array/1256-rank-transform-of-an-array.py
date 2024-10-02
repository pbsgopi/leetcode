class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        ranks = list(sorted(set(arr)))
        for i in range(len(arr)):
            arr[i] = bisect_left(ranks, arr[i]) + 1
        return arr