class Solution:
    def isHappy(self, n: int) -> bool:
        slow, fast = n, n
        slow = self.sumsqr(slow)
        fast = self.sumsqr(self.sumsqr(fast))
        if slow==1 or fast==1:
            return True

        while slow!=fast:
            if fast == 1:
                return True
            slow = self.sumsqr(slow)
            fast = self.sumsqr(self.sumsqr(fast))
        return False    
    def sumsqr(self, n):
        sum = 0
        while n>0:
            ld = n%10
            sum += ld**2
            n = n//10
        return sum