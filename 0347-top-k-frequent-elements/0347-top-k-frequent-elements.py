class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_table = Counter(nums)
        heap = []
        for i in freq_table.keys():
            heappush(heap, (freq_table[i], i))
        freq_table = nlargest(k,heap)
        ans = []
        for i, j in freq_table:
            ans.append(j)
        return ans