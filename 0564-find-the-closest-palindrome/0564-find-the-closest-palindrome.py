class Solution:
    def nearestPalindromic(self, n: str) -> str:
        if int(n) < 10:
            return str(int(n) - 1)
        elif n == '1' + '0' * (len(n) - 1):
            return str(int(n) - 1)
        
        length = len(n)
        if length % 2 == 0:
            lstr = n[:length // 2]
            lnum = int(lstr)
        else:
            lstr = n[:length // 2 + 1]
            lnum = int(lstr)

        candidates = set()
        for diff in [-1, 0, 1]:
            curr_left = lnum + diff
            if length % 2 == 0:
                right = str(curr_left)
                candidates.add(str(curr_left) + right[::-1])
            else:
                right = str(curr_left)
                candidates.add(str(curr_left) + right[-2::-1])
        
        temp1 = '1' + '0' * (len(n) - 1) + '1'
        temp2 = '9' * (len(n) - 1)
        candidates.add(temp1)
        candidates.add(temp2)

        candidates.discard(n)
        min_diff = float('inf')
        nearest_palindrome = ""
        for can in candidates:
            diff = abs(int(can) - int(n))
            if diff < min_diff or (diff == min_diff and int(can) < int(nearest_palindrome)):
                min_diff = diff
                nearest_palindrome = can

        return nearest_palindrome