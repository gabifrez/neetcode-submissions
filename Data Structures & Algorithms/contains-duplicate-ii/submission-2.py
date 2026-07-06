class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        indices = {}
        for i in range(len(nums)):
            if nums[i] not in indices:
                indices[nums[i]] = []
            indices[nums[i]].append(i)
    
        for key in indices:
            if len(indices[key]) < 2:
                continue
            if abs(indices[key][-1] - indices[key][-2]) <= k:
                return True
        return False
            
