# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        def concatenate(arr, start, middle, end):
            L = arr[start:middle+1]
            R = arr[middle+1:end+1]

            i = 0
            j = 0
            k = start

            while i < len(L) and j < len(R):
                if L[i].key > R[j].key:
                    arr[k] = R[j]
                    j+=1
                else:
                    arr[k] = L[i]
                    i+=1
                k+=1
            while i < len(L):
                arr[k] = L[i]
                k+=1
                i+=1
            while j < len(R):
                arr[k] = R[j]
                k+=1
                j+=1

                

        def sort(arr, start, end):
            if end - start + 1 <= 1:
                return arr
            
            middle = (start + end) // 2
            sort(arr, start, middle)
            sort(arr, middle + 1, end)

            concatenate(arr, start, middle, end)

            return arr

        return sort(pairs, 0, len(pairs) - 1)

