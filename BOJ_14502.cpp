// https://www.acmicpc.net/problem/14502
// 삼성 연구소
#include <vector>
#include <iostream>
#include <algorithm>
#include <stack>

using namespace std;

int N, M;
vector<vector<int>> grid;
vector<vector<int>> seen;
vector<pair<int,int>> virus;
vector<pair<int,int>> space; // empty space

int n_walls = 0;
int ans = 64;
int xmoves[] = {0,0,1,-1};
int ymoves[] = {1,-1,0,0};

bool isValid(int x, int y){
    // inside the map and the cell is empty
    if (0 > x || x >= N || 0 > y || y >= M) return false;
    if (grid[x][y] == 1) return false;

    return true;
}

int dfs(){
    stack<pair<int,int>> st;
    for (auto p:virus) {
        st.push(p);
        seen[p.first][p.second] = 1;
    }
    int cnt = 0; // count of virus. Should be minimized.
    while (!st.empty()) {
        pair<int, int> curr = st.top();
        st.pop();
        cnt++;
        if (cnt >= ans) break; // early stopping b/c too much virus
        for (int idx=0; idx<4; idx++){
            int nx = curr.first + xmoves[idx];
            int ny = curr.second + ymoves[idx];
            if (isValid(nx, ny) && seen[nx][ny] == 0){
                seen[nx][ny] = 1;
                st.push(pair(nx,ny));
            }
        }
    }
    return cnt;
}

void check_grid(){
    cout << "=========================" <<endl;
    for (int n=0; n < N; n++) {
        for (int m=0; m < M; m++) {
            cout << grid[n][m] << " ";
        }
        cout << "" << endl;
    }
}

void build_walls(int idx, int sum){
    if (sum == 3){
        seen.resize(N, vector<int>(M, 0));
        int virus_cnt = dfs();
        ans = min(ans, virus_cnt);
        if (ans == virus_cnt){
            check_grid();
        }
        return ;
    } else if (idx > space.size()-1) {
        return ;
    }
    // vector<vector<int>> temp;
    // for (int r=0; r<N; r++){
    //     for (int c=0; c<M; c++){
    //         temp[r][c] = grid[r][c];
    //     }
    // }
    // build wall at space[idx]
    grid[space[idx].first][space[idx].second] = 1;
    build_walls(idx+1, sum+1);
    
    // backtracking
    grid[space[idx].first][space[idx].second] = 0;
    build_walls(idx+1, sum);
}


int main(){
    cin >> N >> M;
    grid.resize(N, vector<int>(M, 0));

    for (int n=0; n < N; n++) {
        for (int m=0; m < M; m++) {
            int x;
            cin >> x;
            grid[n][m] = x;
            if (x == 2) {
                virus.push_back(pair(n,m));
            } else if (x == 1) {
                n_walls++;
            } else if (x == 0) {
                space.push_back(pair(n,m));
            }
        }
    }
    build_walls(0, 0);
    cout << "ans: " <<ans << " n_walls: " <<n_walls <<endl;
    cout << N*M - n_walls - 3 - ans;
}