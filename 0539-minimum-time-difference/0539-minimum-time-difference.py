class Solution:
    def findMinDifference(self, time: List[str]) -> int:
        def minute(a):
            return int(a[:2]) * 60 + int(a[-2:])
        time.sort()
        ans = 12 * 60
        for i in range(len(time)):
            j = (i + 1) % len(time)
            ans = min(ans, (minute(time[j]) - minute(time[i])) % 1440)
        return ans