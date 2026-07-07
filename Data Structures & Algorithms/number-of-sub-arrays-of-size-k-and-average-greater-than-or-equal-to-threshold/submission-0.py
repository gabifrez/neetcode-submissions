class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        suma, counter, left = 0, 0, 0
        for i in range(k):
            suma+= arr[i]
        for i in range(k, len(arr)):
            if suma // k >= threshold:
                counter += 1
            suma -= arr[left]
            suma += arr[i]
            left += 1
        if suma // k >= threshold:
                counter += 1
        return counter