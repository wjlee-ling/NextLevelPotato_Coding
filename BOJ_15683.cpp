#include<iostream>
#include<vector>
using namespace std;

int N,M,C, res, ans = INT_MAX; //가로, 세, 카메라수, 감시되는 수
int map[8][8];
pair<int,int> moves[4] = {{-1,0}, {0,1}, {1,0}, {0,-1}};
vector<pair<int,int>> v; // coordinates of each camera
vector<int> cctv[6];

void copymap(int (*a)[8], int (*b)[8]) {
    for (int i = 0; i <N; i++) {
        for (int j = 0; j < M; j++) {
            a[i][j] = b[i][j];
        }
    }
    return ;
}

void dfs(int idx) {

    if (idx >= C){
        if (ans > res) {
            ans = res;
        }
        return ;
    }

    int cr = v[idx].first, cc = v[idx].second;
    int spin = 0;
    int cnum = map[cr][cc];
    spin = (cnum == 1) ? 4 : ( (cnum == 2) ? 2 : ( (cnum == 3) ? 4 : cnum == 4 ? 4 : 1)); // 회전 수

    for (int i = 0; i < spin; i++){
        int temp[8][8];
        int restemp = res;
        copymap(temp, map);
        for (int j = 0; j<cctv[cnum].size(); j++) {
            int lonum = cctv[cnum][j] + i > 3 ? cctv[cnum][j]+i-4 : cctv[cnum][j]+i;
            int r = cr + moves[lonum].first;
            int c = cc + moves[lonum].second;
            while (r < N && c < M && r >= 0 && c >= 0 && map[r][c] != 6) {
                if (map[r][c]==0) {
                    map[r][c] = -1;
                    res--; // 0 -> #
                }
                r += moves[lonum].first;
                c += moves[lonum].second;
            } 
        }
        dfs(idx+1);
        copymap(map, temp);
        res = restemp;
    }
}

int main(){
    cin >> N >> M;
    res = N * M;
    for (int i = 0; i < N; i++){
        for (int j = 0; j < M; j++) {
            cin >> map[i][j];
            if (map[i][j] != 0 && map[i][j] != 6) {
                v.push_back({i,j});
            }
            if (map[i][j] != 0) {
                res--;
            } 
        }
    }
    C = v.size();
    cctv[1] = {1};
    cctv[2] = {1,3};
    cctv[3] = {0,1};
    cctv[4] = {0,1,3};
    cctv[5] = {0,1,2,3};
    dfs(0);
    cout << ans << endl;
}