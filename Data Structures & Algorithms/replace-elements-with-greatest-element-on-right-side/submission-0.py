class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)-2
        temp = arr[-1]
        while n!=-1:
            curr = temp
            temp = arr[n]
            arr[n] = max(curr, arr[n+1])
            n-=1
        arr[-1] = -1
        return arr

