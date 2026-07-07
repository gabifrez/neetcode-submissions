class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        suma, minim, left, size = 0, 0, 0, 0
        for i in range(len(nums)):
            suma += nums[i]
            size += 1
            if suma >= target:
                if minim == 0:
                    minim = size
                while True:
                    if suma - nums[left] < target:
                        if minim > size:
                            minim = size
                        break
                    suma -= nums[left]
                    left += 1
                    size -= 1

        return minim