// https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/discuss/355940/C%2B%2B-Coin-Change-2
class Solution {
public:
    // dp(d, f, target) = dp(d-1, f, target-1) + dp(d-1, f, target-2) + ... + dp(d-1, f, target-f)
    int dp[31][1001] = {};
    int numRollsToTarget(int n, int k, int target, int res=0) {
        if (n==0 || target <=0) return n==target; //n== target==0 (i.e. zero dice => 0)
        if (dp[n][target]) return dp[n][target]-1;  
        for (auto i=1; i<=k; i++){
            res = (res + numRollsToTarget(n-1,k,target-i)) % 1000000007;    
        }
        dp[n][target] = res+1; // b/c the dp vector is initialized w/ 0
        return res;
    }
};