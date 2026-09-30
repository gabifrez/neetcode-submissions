class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        minBuy = prices[0]
        for price in prices:
            result = max(result, price - minBuy)
            minBuy = min(minBuy, price)
        return result

