class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] += 1
            return digits
        remainder, i = 0, 1
        while i <= len(digits) and digits[-i] == 9:
            digits[-i] = 0
            remainder = 1
            i+=1
        if i > len(digits):
            return [1] + digits
        digits[-i] += 1
        return digits
        
