class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        count = Counter((s1 + ' ' + s2).split(' '))
        res = []
        for i in count.keys():
            if count[i] < 2:
                res.append(i)
        return res