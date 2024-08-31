class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0 for _ in range(n)]
        for i in range(n):
            while stack and temperatures[i]>temperatures[stack[-1]]:
                temp = stack.pop()
                ans[temp] = i-temp
            stack.append(i)
        return ans