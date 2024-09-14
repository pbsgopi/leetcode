class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        xorarr = []
        temp = 0
        for i in arr:
            temp ^= i
            xorarr.append(temp)

        ans = []
        for i, j in queries:
            if i == 0:
                ans.append(xorarr[j])
            else:
                ans.append(xorarr[j] ^ xorarr[i - 1])
        return ans