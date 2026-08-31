class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set()
        left = 0
        for i in range(len(nums)):
            if i > k:
                visited.remove(nums[left])
                left+=1 
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        return False