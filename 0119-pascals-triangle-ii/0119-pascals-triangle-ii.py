class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        dp=[]
        for i in range(rowIndex+1):
            row=[1]*(i+1)
            for j in range(1,i):
                row[j]=dp[i-1][j-1]+dp[i-1][j]
            dp.append(row)
        return dp[rowIndex]