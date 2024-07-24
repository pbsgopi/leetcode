
class Solution:
    def countAndSay(self, n: int) -> str:
        result = ''
        def count(string):
            new_string = ''
            c = 1
            previous = string[0]
            for i in range(1, len(string)):
                if string[i] == previous:
                    c += 1
                else:
                    new_string += str(c) + previous
                    c = 1
                    previous = string[i]

            new_string += str(c) + previous

            return new_string

        def helper(n, result):
            if n == 1:
                return '1'
            result += count(helper(n-1, result))
            return result
        return helper(n, result)