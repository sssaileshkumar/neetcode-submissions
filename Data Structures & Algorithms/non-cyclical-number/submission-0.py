class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        def sumOfDigits(n):
            n = str(n)
            total = 0
            for i in n:
                total += int(i)**2
            return total

        def recurssion(n):
            if n == 1:
                return True
            if n in seen:
                return False
            
            seen.add(n)
            return recurssion(sumOfDigits(n))
        
        return recurssion(n)