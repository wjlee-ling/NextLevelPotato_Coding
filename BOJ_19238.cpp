#include <vector>
#include <iostream>
#include <queue>
#include <cstring>
using namespace std;

vector<vector<int> > graph(21, vector<int>(21, 1));
vector<vector<int>> passengers(21, vector<int>(21,-1)), destinations(21, vector<int>(21,-1));
vector<int> xmoves = {-1,0,0,1};
vector<int> ymoves = {0,-1,1,0};
int N, M, gas, origin_x, origin_y, ret;

struct Coord{
    int x;
    int y;
    int d;
    Coord(int cx, int cy, int cd): x(cx), y(cy), d(cd) {}
};

int bfs(vector<vector<int>>& pass, vector<vector<int>>& dest, int x, int y, int gas, int del_num) {
    queue<Coord> q;
    vector<vector<int>> seen(21, vector<int>(21, 1));
    // Coord ele(x, y, 0);
    int taxi_num=-1, ret=-1;
    bool search_pass = true;
    if (del_num==0) return gas;

    q.push(Coord(x, y, 0));
    seen[x][y] = 0;
    while (!q.empty()) {
        int cx, cy, cd;
        cx = q.front().x, cy = q.front().y, cd = q.front().d;
        cout << "x " << cx << " y: " << cy << " d: " << cd << endl;
        q.pop();
        // find the closest passenger (i.e. no specific target)
        if (pass[cx][cy]!=-1 && search_pass) {
            taxi_num = pass[cx][cy]; // taxi idx
            pass[cx][cy] = -1;
            // seen.resize(21, vector<int>(21, 1)); // reset seen
            for (auto& row:seen) {
                row.assign(row.size(), 1);
            }
            search_pass = false;
            seen[cx][cy] = 0;
            gas -= cd;
            // std::cout << "passenger: " << taxi_num  << "-> x: "<< cx << " y: "  << cy << " gas: " << gas << endl;
            if (gas <= 0) return -1;
            q = {};
            for (int i=0; i<4; i++) {
                int dx, dy, nx, ny;
                dx = xmoves[i], dy = ymoves[i];
                nx = cx+dx, ny = cy+dy;
                if (nx < 0 || nx > 20 || ny <0 || ny > 20) continue;
                if (graph[nx][ny] != 1 && seen[nx][ny]){
                    q.push(Coord(nx,ny,1));
                    seen[nx][ny] = 0;
                }
            }
        }
        else if (dest[cx][cy] == taxi_num && dest[cx][cy] != -1) {
            // get to the destination
            dest[cx][cy] = -1;
            if (gas - cd < 0) return -1; // out of gas on the way to the destination
            if (gas + cd <0) return -1; // out of gas even after being gased
            // std::cout << "dest: " << taxi_num  << "-> cx: "<< cx << " cy: "  << cy << " gas refilled: " << gas+cd << endl;
            ret = bfs(pass, dest, cx, cy, gas+cd, del_num-1);
            return ret;

        }
        else {
            for (int i=0; i<4; i++) {
                int dx, dy, nx, ny;
                dx = xmoves[i], dy = ymoves[i];
                nx = cx+dx, ny = cy+dy;
                // cout << "N: " << N << "  " <<nx << ny << endl;
                if (nx < 0 || nx > 20 || ny <0 || ny > 20) continue;
                if (graph[nx][ny] != 1 && seen[nx][ny]){
                    q.push(Coord(nx,ny,cd+1));
                    seen[nx][ny] = 0;
                }
            }
        }

    }
    return ret;
}


int main(){
    
    cin >> N >> M >> gas;
    for (int i=1; i<N+1; i++){
        for (int j=1; j<N+1; j++) {
            cin >> graph[i][j]; 
        }
    }
    cin >> origin_x >> origin_y;

    // vector<vector<int>> passengers(M+1, vector<int>(M+1,-1)), destinations(M+1, vector<int>(M+1,-1));
    for (int i=0; i<M; i++){
        int a,b,c,d;
        cin >> a >> b >> c >> d;
        passengers[a][b] = i;
        destinations[c][d] = i;
    }
    ret = bfs(passengers, destinations, origin_x, origin_y, gas, M);
    cout << ret;
}