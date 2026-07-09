class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # starting_point = -1
        # max_sum = suma = 0
        # n = len(nums)

        # for i in range(n*2 - 1):
        #     if starting_point == i % n:
        #         break
        #     suma = max(suma, 0)
        #     if suma == 0:
        #         starting_point = i
        #     suma += nums[i%n]
        #     max_sum = max(suma, max_sum)

        # return max_sum

        globalMax = globalMin =  nums[0]
        curMax = curMin = total = 0
        for number in nums:
            total += number
            curMax = max(curMax + number, number)
            curMin = min(curMin + number, number)
            globalMax = max(curMax, globalMax)
            globalMin = min(curMin, globalMin)
        if globalMax < 0:
            return globalMax
        return max(globalMax, total - globalMin)
