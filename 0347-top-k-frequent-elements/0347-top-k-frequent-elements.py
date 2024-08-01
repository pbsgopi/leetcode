class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        top = counter.most_common(k)
        return [key for key, count in top]