class Solution {
public:
    int R;
    int C;
    int xmoves[4] = {0,0,1,-1};
    int ymoves[4] = {1,-1,0,0};
    
    int minimumEffortPath(vector<vector<int>>& heights) {
        R = heights.size();
        C = heights[0].size();
        int left=0, right=0;
        
        // set right at the maximum
        for (auto& row: heights){
            for (int h: row){
                right = max(right, h);
            }
        }
        
        while (left <= right){
            int mid = left + (right-left)/2;
            if (check(mid, heights)){
                // since we're looking for the minimum
                right = mid-1;
            } else {
                left = mid+1;
            }
        }
        return left;
    }
    
    bool check(int effort, vector<vector<int>>& heights){
        vector<vector<bool>> seen(R, vector<bool>(C, false));
        stack<pair<int,int>> st;
        seen[0][0] = true;
        st.push(pair(0,0));
        
        while (!st.empty()){
            auto [cx, cy] = st.top();
            st.pop();
            
            if (cx==R-1 && cy==C-1) return true;
            
            
            for (int idx=0; idx<4; idx++) {
                int nx = cx + xmoves[idx];
                int ny = cy + ymoves[idx];
                if (0<=nx && nx<R && 0<=ny && ny<C && !seen[nx][ny]){
                    if (abs(heights[nx][ny]-heights[cx][cy]) <= effort){
                        st.push(pair(nx,ny));
                        seen[nx][ny] = true;
                    }
                }
            }
        }
        return false;
    }
};
//     // 1st try: Time limit exceeded!! 
//     int diff = INT_MAX; // should be smallest

//     void step(int cx, int cy, int max_effort, vector<vector<int>>& heights, vector<vector<int>>& visited) {
//         int X = heights.size(), Y = heights[0].size();
//         int xmoves[4] = {0, 0, -1, 1};
//         int ymoves[4] = {1, -1, 0, 0};

//         if (cx == X - 1 && cy == Y - 1) {
//             diff = min(max_effort, diff);
//             return;
//         }

//         for (int i = 0; i < 4; i++) {
//             int nx = cx + xmoves[i];
//             int ny = cy + ymoves[i];
//             if (0 <= nx && nx < X && 0 <= ny && ny < Y && visited[nx][ny] == 0) {
//                 visited[nx][ny] = 1;
//                 int effort = abs(heights[nx][ny] - heights[cx][cy]);
//                 int temp_max_effort = max(max_effort, effort);
//                 if (temp_max_effort > diff) continue;
//                 step(nx, ny, temp_max_effort, heights, visited);
//                 visited[nx][ny] = 0;
//             }
//         }
//     }

//     int minimumEffortPath(vector<vector<int>>& heights) {
//         int X = heights.size(), Y = heights[0].size();
//         vector<vector<int>> visited(X, vector<int>(Y, 0));

//         visited[0][0] = 1;
//         step(0, 0, 0, heights, visited);
//         return diff;
//     }    
    
