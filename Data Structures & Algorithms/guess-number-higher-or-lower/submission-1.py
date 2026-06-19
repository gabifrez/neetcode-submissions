# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            number = (left + right) // 2
            if guess(number) == -1:
                right = number - 1
            elif guess(number) == 1:
                left = number + 1
            else:
                return number