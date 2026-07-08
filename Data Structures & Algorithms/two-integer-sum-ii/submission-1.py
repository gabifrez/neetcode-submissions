class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        result = numbers[left] + numbers[right]
        while result != target:
            result = numbers[left] + numbers[right]
            if result > target:
                right -= 1
            if result < target:
                left += 1


        return [left + 1, right + 1]