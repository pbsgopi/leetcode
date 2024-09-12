class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            count+=1
            for j in i:
                if j not in allowed:
                    count-=1
                    break
        return count