class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1 = min(prices[0], prices[1])
        min2 = max(prices[0], prices[1])
        for i in range(2, len(prices)):
            temp = min2
            if min2 >= prices[i]:
                if min1 <= prices[i]:
                    min2 = prices[i]
                else:
                    min1, min2 = prices[i], min1

        if min1 + min2 <= money:
            return money - min1 - min2
        return money