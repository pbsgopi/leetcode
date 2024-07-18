class Solution {
public:
    int change(int amount, vector<int>& coins) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);
        cout.tie(NULL);
        
        int n = coins.size();
        vector<vector<int>> dp(n+1,vector<int>(amount+1));
        int i,j;
        for(i=1;i<=amount;++i)
            dp[0][i] = 0;
        for(i=0;i<=n;++i)
            dp[i][0] = 1;
        
        for(i=1;i<=n;++i)
        {
            for(j=1;j<=amount;++j)
            {
                if(j>=coins[i-1])
                    dp[i][j] = dp[i][j-coins[i-1]]+dp[i-1][j];
                else
                    dp[i][j] = dp[i-1][j];
            }
        }
        return dp[n][amount];
    }
};