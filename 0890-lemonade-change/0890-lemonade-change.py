class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives=0
        tens=0
        twos=0
        for i in bills:
            if i==5:
                fives+=1
            elif i==10:
                tens+=1
                fives-=1
                if fives<0:
                    return False
            else:
                twos+=1
                if tens>=1 and fives>=1:
                    tens-=1
                    fives-=1
                elif tens<1 and fives>=3:
                    fives-=3
                else:
                    return False
        return True