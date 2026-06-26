class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        array, current = [], []
        def backtrack(index, n, k, array, current):
            if len(current) == k:
                array.append(current.copy())
                return
            
            if index > n:
                return
            
            for i in range(index, n+1):
                current.append(i)
                backtrack(i+1,n,k,array,current)
                current.pop()

        backtrack(1, n, k, array, current)
        return array
        