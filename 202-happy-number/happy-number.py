class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            total = 0
            while n > 0:
                d = n%10
                total += d * d
                n = n//10
            n = total
        if n == 1:
            return True
        else:
            return False
