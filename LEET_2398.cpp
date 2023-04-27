// https://leetcode.com/problems/maximum-number-of-robots-within-budget/
// stacks and queues
#include <vector>
#include <algorithm>
#include <deque>
using namespace std;
class Solution {
public:
    int maximumRobots(vector<int>& chargeTimes, vector<int>& runningCosts, long long budget) {
        size_t N = chargeTimes.size();
        int left = 0;
        deque<int> dq; // indices in decreasing order
        long long cumsum = 0;
        int ans = 0;
        for (int right=0; right < N; right++) {
            // update dq 
            while (!dq.empty() && chargeTimes[dq.back()] < chargeTimes[right]){
                dq.pop_back();
            }
            dq.push_back(right);
            cumsum += runningCosts[right];
            
            // calculate weighted sum w/ current left and right
            long long cand = cumsum*(right-left+1) + chargeTimes[dq.front()];
            // resize window
            while (right >= left && cand > budget) {
                cumsum -= runningCosts[left];
                left++;
                while (!dq.empty() && dq.front() < left) {
                    dq.pop_front();
                }
                if (!dq.empty()) cand = cumsum*(right-left+1) + chargeTimes[dq.front()]; // 여기서 dq이 비는 걸 예상 못해서 에러 많이 났음!!
                //cout << "l: " << left << " r: " << right << " cumsum: " << cumsum << endl;
            }
            ans = max(ans, right-left+1);
        }
        return ans;
    }
};