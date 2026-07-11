class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = total = 0
        hashmap = {0:1}
        for number in nums:
            total += number
            if total - k in hashmap:
                result += hashmap[total-k]
            if total not in hashmap:
                hashmap[total] = 0
            hashmap[total] +=1
        return result