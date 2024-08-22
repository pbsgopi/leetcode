class Solution:
    def findComplement(self, num: int) -> int:
        binary=bin(num)
        complement=''
        for i in range(len(binary)):
            if i > 1:
                if binary[i] == '0':
                    complement +='1'
                else:
                    complement += '0'
        return int(complement,2)