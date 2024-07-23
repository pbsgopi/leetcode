class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy, sell = [inf]*k, [0]*k
        for x in prices:
            for i in range(k): 
                if i: buy[i] = min(buy[i], x - sell[i-1])
                else: buy[i] = min(buy[i], x)
                sell[i] = max(sell[i], x - buy[i])
        return sell[-1]