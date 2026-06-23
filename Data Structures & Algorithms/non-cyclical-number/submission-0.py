class Solution:
    def isHappy(self, n: int) -> bool:
        results = []

        def squareSum(n):
            suma = 0
            while n != 0:
                suma += (n%10)**2
                n//=10
            return suma
        
        while True:
            n = squareSum(n)
            if n == 1:
                return True
                break
            if n in results:
                return False
                break
            results.append(n)