class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sets, current = [],[]

        def backtrack(index, n, k, sets, current):
            if len(current) == k:
                sets.append(current.copy())
                return
            if index > n:
                return
            
            current.append(index)
            backtrack(index + 1, n, k, sets, current)
            current.pop()
            backtrack(index + 1, n, k, sets, current)
        backtrack(1, n, k, sets, current)

        return sets