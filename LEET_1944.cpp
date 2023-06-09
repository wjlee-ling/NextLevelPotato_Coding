#include <vector>
#include <stack>

using namespace std;
class Solution {
public:
    vector<int> canSeePersonsCount(vector<int>& heights) {
        int n = heights.size();
        vector<int> ans(n);
        stack<int> st;
        for (int i = n-1; i >= 0; i--) { // 뒤에서
            while (!st.empty() && heights[i] > st.top()) { // 오른쪽에 있는 작은 애들 봄
                st.pop();
                ans[i]++; // [i+1,] 에서 더 작은 것들
            }
            if (!st.empty())
                ans[i]++; // 현재 있는 것이 최장신이 아님 == 최장신을 볼 수 있음 
            st.push(heights[i]);
        }
        return ans;
    }
};