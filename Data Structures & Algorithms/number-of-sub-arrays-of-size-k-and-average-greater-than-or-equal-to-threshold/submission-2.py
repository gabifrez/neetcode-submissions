class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold = threshold * k
        total, left = 0, 0
        result = 0

        for right in range(len(arr)):
            total += arr[right]
            if right >= k - 1:
                if total >= threshold:
                    result += 1
                total -= arr[left]
                left += 1

        return result 