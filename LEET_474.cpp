#include <vector>
#include <algorithm>
using namespace std;

//https://www.youtube.com/watch?v=qkUZ87NCYSw
class Solution {
public:
    // knapsack 
    int findMaxForm(vector<string>& strs, int m, int n) {
        vector<vector<int>> dp(m+1,vector<int>(n+1,0));

        for (auto& s: strs) {
            int curr_ones = count(s.begin(), s.end(), '1');
            int curr_zeros = s.size()-curr_ones;
            for (int i=m; i>=curr_zeros; i--) // i.e.  m-count(0) >= i  >= 0
                for (int j=n; j>=curr_ones; j--)
                    dp[i][j] = max(dp[i][j], dp[i-curr_zeros][j-curr_ones]+1);
        }
        return dp[m][n];
    }
};