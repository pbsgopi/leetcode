class Solution:
    def longestPalindrome(self, S: str) -> str:
        for i in range(len(S),-1,-1):
            for j in range(len(S)-i+1):
                rev = S[j:j+i]
                if rev == rev[::-1]:
                    return rev