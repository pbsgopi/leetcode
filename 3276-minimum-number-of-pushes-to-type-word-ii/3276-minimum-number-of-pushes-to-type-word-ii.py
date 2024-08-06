class Solution:
    def minimumPushes(self, word: str) -> int:
        count=Counter(word)
        freqArr = list(count.values())
        freqArr.sort(reverse=True)
        res=0
        for i in range(len(freqArr)):
            if i<8:
                res+=(1*freqArr[i])
            elif i<16:
                res+=(2*freqArr[i])
            elif i<24:
                res+=(3*freqArr[i])
            else:
                res+=(4*freqArr[i])
        return res