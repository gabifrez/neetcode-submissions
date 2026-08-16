class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target = k * threshold
        current_sum, result, left = 0, 0, 0
        for i in range(len(arr)):
            current_sum += arr[i]
            if i - left + 1 >= k:
                result += current_sum >= target
                current_sum -= arr[left]
                left += 1
        return result