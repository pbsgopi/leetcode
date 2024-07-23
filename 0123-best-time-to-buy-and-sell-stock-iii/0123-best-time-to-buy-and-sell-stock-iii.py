class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = [inf]*2, [0]*2
        for x in prices:
            for i in range(2): 
                if i: buy[i] = min(buy[i], x - sell[i-1])
                else: buy[i] = min(buy[i], x)
                sell[i] = max(sell[i], x - buy[i])
        return sell[1]