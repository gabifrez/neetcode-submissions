class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {}
        for index, number in enumerate(nums2):
            dic[number] = index
        result = []
        for number in nums1:
            result.append(dic[number])
        return result