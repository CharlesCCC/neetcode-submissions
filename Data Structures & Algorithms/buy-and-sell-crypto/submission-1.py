class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0;
        minBuy = prices[0];
        # DP approach 
        for sell in prices:
            maxP = max(maxP, sell - minBuy) #find the next highest profit 
            minBuy = min(minBuy, sell)  #find the next lowest selling price 

        return maxP;