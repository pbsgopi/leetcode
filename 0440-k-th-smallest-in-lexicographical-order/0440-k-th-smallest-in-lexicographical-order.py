class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        if k == 1:
            return 1
        nstr = str(n)

        @cache
        def opt(i, dig):
            if i == len(nstr):
                return 0

            if int(nstr[:i+1]) > int(dig):
                temp = 0
                for x in range(i, len(nstr)-1):
                    temp+=pow(10, x-i)
                return temp + pow(10, len(nstr)-i-1)

            elif int(nstr[:i+1])<int(dig):
                temp = 0
                for x in range(i, len(nstr)-1):
                    temp+=pow(10, x-i)
                return temp

            else:
                temp = 1
                for x in "1234567890":
                    temp+=opt(i+1,dig+x)

                return temp

        s = "0123456789"
        h = 1

        res = ""
        curr = 0
        ind = 0
        while True:
            x = s[h]
            y = opt(ind, res+x)
            if curr + y>=k:
                res += x
                curr+=1
                if curr == k:
                    return int(res)
                h = 0
                ind+=1
            else:
                curr+=y
                h+=1