class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = [1]
        i = j = k = 0
        count = 0
        
        while count < n:
            val = min(res[i]*2,min(res[j]*3,res[k]*5))
            if val == res[i]*2:
                i+=1
            if val == res[j]*3:
                j+=1
            if val == res[k]*5:
                k+=1
            count+=1
            if count == n:
                return res[-1]
            res.append(val)