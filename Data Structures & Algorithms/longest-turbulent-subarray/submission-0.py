class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = cnt = 0
        sign = -1
        for i in range(len(arr) - 1):
            if arr[i] > arr[i+1]:
                if sign == 1:
                    cnt += 1
                else:
                    cnt = 1
                sign = 0
            elif arr[i] < arr[i+1]:
                if sign == 0:
                    cnt += 1
                else:
                    cnt = 1   
                sign = 1              
            else:
                sign = -1
                cnt = 0
            result = max(result, cnt)
        return result + 1

