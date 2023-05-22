// ref. https://yabmoons.tistory.com/718

#include <vector>
#include <iostream>
#include <algorithm>
#include <unordered_map>
#include <queue>
using namespace std;

int R,C,K,W,ans=0;
struct Heater {
    int r;
    int c;
    int dir; // d:1 -> R, 2 ->L, 3-> Up, 4->Down 
};
vector<vector<int>> graph;
vector<vector<int>> hist;
vector<Heater> heaters;
vector<pair<int,int>> testers;
unordered_map<int, vector<pair<int,int>>> hwalls; // 가로벽
unordered_map<int, vector<pair<int,int>>> vwalls; // 세로벽

int dx[5] = {0,0,0,-1,1};
int dy[5] = {0,1,-1,0,0};
int wdx[5][3] = {{0,0,0}, {-1,0,1}, {-1,0,1}, {-1,-1,-1}, {1,1,1}};
int wdy[5][3] = {{0,0,0}, {1,1,1}, {-1,-1,-1}, {-1,0,1}, {-1,0,1}};

bool is_wall(int cx, int cy, int nx, int ny, int dir){
    int interim;
    if (dir<=2) {
        interim = (nx<cx) ? cx-1 : (nx>cx) ? cx+1 : cx;
        if ( find(hwalls[cy].begin(), hwalls[cy].end(), make_pair(cx,interim)) == hwalls[cy].end() ) {
            // 세로로 벽이 없임
            if (find(vwalls[interim].begin(), vwalls[interim].end(), make_pair(cy,ny)) == vwalls[interim].end()){
                //가로로 없음
                return true;
            } 
        }
    }
    else {
        interim = (ny<cy) ? cy-1 : (ny>cy) ? cy+1 : cy;
        if ( find(vwalls[cx].begin(), vwalls[cx].end(), make_pair(cy,interim)) == vwalls[cx].end() ) {
            if (find(hwalls[interim].begin(), hwalls[interim].end(), make_pair(cx,nx)) == hwalls[interim].end()){
                return true;
            }
        }
    }
    return false;
}

void dispense(Heater& heater){
    int x,y,dir, level = 5;
    queue<pair<pair<int,int>,int>> q;
    fill(hist.begin(), hist.end(), vector<int>(C,1));
    dir = heater.dir;
    // cout << "new heater: " << heater.r << heater.c << heater.dir << endl;
    q.push(make_pair(make_pair(heater.r+dx[dir], heater.c+dy[dir]), level));
    hist[heater.r][heater.c] = 0;
    while (!q.empty()){
        int cx = q.front().first.first;
        int cy = q.front().first.second;
        int l = q.front().second;
        
        q.pop();
        graph[cx][cy] += l; // add heat
        if (l == 1) continue;
        for (int i=0; i<3; i++){
            int nx = cx + wdx[dir][i];
            int ny = cy + wdy[dir][i];
            if (0<=nx<R && 0<=ny<C && hist[nx][ny] && is_wall(cx,cy,nx,ny,dir)) {
                hist[nx][ny] = 0;
                q.push(make_pair(make_pair(nx,ny), l-1));
            }
        }
    }
}

void control(){
    // 온도조절, 우하로만
    int temp_graph[20][20] = {0,};
    for (int x=0; x<R; x++) {
        for (int y=0; y<C; y++) {
            for (int i=0; i<2; i++) {
                int dir = (i==0) ? 1 : 4;
                int nx = x+dx[dir];
                int ny = y+dy[dir];
                // cout << nx << ny << dir ;
                if (nx>=0 && nx<R && ny>=0 && ny <C) {
                    if (is_wall(x,y,nx,ny,dir)) {
                        int diff = abs(graph[nx][ny] - graph[x][y]);
                        diff /= 4;
                        if (graph[nx][ny] > graph[x][y]) {
                            temp_graph[nx][ny] -= diff;
                            temp_graph[x][y] += diff;
                        } else {
                            temp_graph[nx][ny] += diff;
                            temp_graph[x][y] -= diff;
                        }
                    }
                }
            }
        }
    }
    for (int i=0; i<R; i++) {
        for (int j=0; j<C; j++) {
            graph[i][j] += temp_graph[i][j];
        }
    }

}

void reduce_edges(){
    for (int r=0; r<R; r++) {
        for (int c=0; c<C; c++) {
            if (r==0 || r==R-1) {
                if (graph[r][c] > 0) {
                    graph[r][c]-=1;
                }
            } else if (c==0 || c==C-1){
                if (graph[r][c] >0) {
                    graph[r][c]-=1;
                }
            }
        }
    }
}

bool check_temp(){
    for (auto const& tester:testers){
        int tr = tester.first, tc = tester.second;
        if (graph[tr][tc] < K) return false;
    }
    return true;
}

int main() {
    cin >> R >> C >> K;
    graph.resize(R, vector<int>(C));
    hist.resize(R, vector<int>(C,1));    
    // get input and build graph
    for (int r=0; r<R; r++) {
        for (int c=0; c<C; c++) {
            cin >> graph[r][c];
            if (graph[r][c]==5) {
                testers.push_back({r,c});
                graph[r][c] = 0; // 조사 칸의 온도 0
            } else if (graph[r][c]>0) {
                heaters.push_back({r,c,graph[r][c]});
                graph[r][c] = 0;
            }
        }
    }
    cin >> W;
    for (int w=0; w<W; w++){
        int x, y, t;
        cin >> x >> y >> t;
        pair<int,int> p;
        x--, y--;
        if (t==0) {
            // 가로
            hwalls[y].push_back(make_pair(x-1,x));
            hwalls[y].push_back(make_pair(x,x-1));
        } else {
            vwalls[x].push_back(make_pair(y,y+1));
            vwalls[x].push_back(make_pair(y+1,y));
        }
    }

    for (auto& h:heaters) {
        dispense(h); 
    }
    control();
    reduce_edges();
    ans++; //eat chocolate

    while (!check_temp()) {
        for (auto& h:heaters) {
            dispense(h);
        }
        control();
        reduce_edges();
        ans++;         
        if (ans>=100){
            ans = 101;
            break;
        }
    }
    cout << ans;
    return 0;
}