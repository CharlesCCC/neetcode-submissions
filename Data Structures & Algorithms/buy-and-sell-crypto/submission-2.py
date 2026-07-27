class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        miniBuy = prices[0]
        for sell in prices:
            maxP = max(maxP, sell-miniBuy)
            miniBuy = min(miniBuy, sell)
        
        return maxP