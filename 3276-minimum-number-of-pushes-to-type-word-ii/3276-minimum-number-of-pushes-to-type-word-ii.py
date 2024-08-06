class Solution:
    def minimumPushes(self, word: str) -> int:
        count=Counter(word)
        freqArr = list(count.values())
        freqArr.sort(reverse=True)
        res=0
        for i, num in enumerate(freqArr):
            res += (((i // 8) + 1) * num)
        return res