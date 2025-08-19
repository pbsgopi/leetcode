class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res=0
        prevEnd=intervals[0][1]
        for i,j in intervals[1:]:
            if i>=prevEnd:
                prevEnd=j
            else:
                res+=1
                prevEnd=min(j,prevEnd)
        return res