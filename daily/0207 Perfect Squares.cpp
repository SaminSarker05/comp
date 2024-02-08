class Solution {
public:
    // top down DP solution with memoization

    int helper(vector<int>& dp, int n) {
        if (n == 0) return 0;
        if (dp[n] != -1) return dp[n];

        int ans = n;
        for (int i = 1; i * i <= n; i++) {
            int square = i * i;
            ans = min(ans, 1 + helper(dp, n - square));
        }
        dp[n] = ans;
        return dp[n];

    }
    int numSquares(int n) {
        vector<int> dp(n+1, -1);
        return helper(dp, n);
    }
};