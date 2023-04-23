#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <cstring>
using namespace std;

int n,m;
int graph[51][51];
const int dc[4] = {0,0,1,-1};
const int dr[4] = {1,-1,0,0};
int zeros;
int ans = -1;

vector<pair<int,int>> origins;

int bfs(vector<pair<int, int>> p) {
    int rest = zeros;
    if (rest == 0) return 0;

    int dist[51][51]; // d+ 4 bumpers
    memset(dist, -1, sizeof(dist));
    queue<pair<int, int>> q;
    for (int i=0; i < p.size(); ++i) {
        int c = p[i].first;
        int r = p[i].second;

        q.push(p[i]);
        dist[c][r] = 0; // origins of virus
    }

    while (!q.empty()) {
        int c = q.front().first;
        int r = q.front().second;
        q.pop();

        for (int i = 0; i < 4; ++i) {
            int nc = c+dc[i];
            int nr = r+dr[i];

            if (!(0 <= nc && nc < n && 0 <= nr && nr < n)) continue; // out of graph
            if (graph[nc][nr] == 1) continue; // wall
            if (dist[nc][nr] != -1) continue; // visited or origins
            
            q.push({nc, nr});
            dist[nc][nr] = dist[c][r] + 1;
            
            if (graph[nc][nr] == 0) {
                rest -= 1;
            }
            if (rest == 0) {
                return dist[nc][nr];
            }
        }
    }
    return -1;
}

void run(vector<pair<int,int>> p, int begin) {
    // get combinations w/ backtracking
    if (p.size() == m) {
        int ret = bfs(p);
        if (ret != -1) {
            if (ans==-1 || ans >ret) {
                ans = ret;
            }
        }
        return ;
    }

    for (int i = begin+1; i < origins.size(); ++i) {
        p.push_back(origins[i]);
        run(p,i);
        p.pop_back();
    }
}

int main() {
    cin >> n >> m;
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            cin >> graph[i][j];
            if (graph[i][j] == 0) {
                zeros += 1;
            }
            if (graph[i][j]== 2) {
                origins.push_back({i,j});
            }
        }
    }
    vector<pair<int,int>> picked;
    run(picked, -1);
    
    cout << ans << "\n";
    return 0;
}