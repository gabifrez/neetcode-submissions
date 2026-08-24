class Solution:
    def reverseBits(self, n: int) -> int:
        index = 1
        result = 0
        for i in range(31, -1, -1):
            if n & index == index:
                result += 2**i
            index <<= 1
        return result