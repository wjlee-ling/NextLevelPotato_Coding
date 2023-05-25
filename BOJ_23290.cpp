// 마법사 상어와 복제
// https://www.acmicpc.net/problem/23290

#include <vector>
#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;


struct Fish {
    int x;
    int y;
    int dir;
    
    Fish(int x, int y, int dir): x(x), y(y), dir(dir){};
    bool operator==(const Fish& other) const {
        return x == other.x && y == other.y && dir == other.dir;
    }
};

int M, S, ans=0;
int R=4, C=4;
int maxi=0, visited[4][4];
string min_str;
Fish shark = Fish(0,0,0);
vector<Fish> fishes;
vector<Fish> kill_list;
vector<vector<vector<Fish>>> graph;
vector<vector<int>> reek;
int xmoves[8] = {0, -1, -1, -1, 0, 1, 1, 1};
int ymoves[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int xs[4] = {-1,0,1,0}; //shark moves 상좌하우
int ys[4] = {0,-1,0,1};

void getInput(){
    int x, y, dir;
    cin >> M >> S;

    graph.resize(R, vector<vector<Fish>>(C));
    reek.resize(R, vector<int>(C));

    for (int i=0; i<M; i++) {
        cin >> x >> y >> dir;
        Fish fish(x-1,y-1,dir-1);
        fishes.push_back(fish);
        graph[x-1][y-1].push_back(fish);
    }
    cin >> shark.x >> shark.y;
    shark.x-=1;
    shark.y-=1;
}

bool canGo(int x, int y){
    return (x >= 0 && x < R && y >= 0 && y<C);
}

vector<Fish> mv_fishes(int step){
    vector<Fish> new_fishes;
    for (auto& fish: fishes) {
        int cx=fish.x, cy=fish.y, dir=fish.dir;
        int dx=xmoves[dir], dy=ymoves[dir];
        int nx=cx+dx, ny=cy+dy;

        // 복사
        new_fishes.push_back(fish);

        while (! (canGo(nx,ny) && reek[nx][ny] != step-1 && abs(nx-shark.x)+abs(ny-shark.y)==0)) {            
            dir = (dir>0) ? (dir-1) % 8 : 7;
            if (dir==fish.dir){
                nx=cx, ny=cy;
                break;
            } else {
                dx=xmoves[dir], dy=ymoves[dir];
                nx=cx+dx, ny=cy+dy;
            }
        }
        fish.x = nx, fish.y = ny, fish.dir = dir;
        vector<Fish>& cell = graph[cx][cy];
        auto it = find(cell.begin(), cell.end(), fish);
        cell.erase(it);
        graph[nx][ny].push_back(fish);
    }
    return new_fishes;
}

void search(int cx, int cy, vector<Fish>& dead_fish, string dirs){
    // 물고기 찾기, 가장 많이 있는 방향의 물고기 넘버 리턴
    if (dirs.size()==3){
        int cnt = dead_fish.size();
        maxi = max(maxi, cnt);
        min_str = to_string(min(stoi(min_str), stoi(dirs))); // lexical_graph order
        if (maxi==cnt && maxi!=0 && min_str == dirs) {
            kill_list = dead_fish;
            shark.x = cx, shark.y = cy;
        } 
        return ;
    }
    for (int i=0; i<4; i++){
        int nx = cx+xs[i];
        int ny = cy+ys[i];
        if (canGo(nx,ny) && visited[nx][ny]==0){
            visited[nx][ny]=1;
            for (Fish fish:graph[nx][ny]){
                dead_fish.push_back(fish);
            }
            search(nx,ny, dead_fish, dirs+to_string(i+1)); // std::to_string
            visited[nx][ny]=0;
            for (int n=0; n<graph[nx][ny].size(); n++) {
                dead_fish.pop_back();
            }
        }
    }
}

void mv_shark(int step){
    vector<Fish> df = {};
    string temp = "";
    maxi = 0;
    min_str = "999";

    memset(visited, 0, sizeof(visited));
    kill_list.clear();
    search(shark.x, shark.y, df, temp);
    // 물고기 죽이기
    for (auto& fish:kill_list) {
        int x, y;
        x = fish.x, y = fish.y;
        graph[x][y].clear(); // 생선 지우기
        reek[x][y] = step; // 현재 스텝의 냄새 남김
        vector<Fish>::iterator it = find(fishes.begin(), fishes.end(), fish);
        fishes.erase(it);
        // fishes.erase(remove(fishes.begin(), fishes.end(), fish), fishes.end());
    }
}

void run_step(int step){
    vector<Fish> new_fishes;

    new_fishes = mv_fishes(step); // 복사랑 이동도 같이
    mv_shark(step);

    for (auto& fish: new_fishes) {
        int x = fish.x;
        int y = fish.y;
        
        graph[x][y].push_back(fish); // 맵에 추가
        fishes.push_back(fish); 
    }
}

int main(){
    int step = 1;
    getInput();
    for (int s=0; s<S; s++) {
        run_step(step++);
    }
    for (int r=0; r <R; r++) {
        for (int c=0; c<C; c++) {
            ans += graph[r][c].size();
        }
    }
    cout << ans;
}