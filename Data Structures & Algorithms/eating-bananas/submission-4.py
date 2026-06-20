class Solution:
    def canFinish(self, piles, rate, target):
        suma = 0
        for pile in piles:
            suma += (pile + rate - 1) // rate
        return suma <= target

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, piles[0]
        for pile in piles:
            if right < pile:
                right = pile
        while left <= right:
            rate = (left+right) // 2
            if self.canFinish(piles, rate, h):
                right = rate - 1
            else:
                left = rate + 1
        return left


        

