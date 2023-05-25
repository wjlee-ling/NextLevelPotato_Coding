// 마법사 상어와 복제
// https://www.acmicpc.net/problem/23290

#include <vector>
#include <iostream>
#include <cstring>

using namespace std;


struct Fish {
    int nr;
    int x;
    int y;
    int dir;
    Fish(int i, int x, int y, int dir): nr(i), x(x), y(y), dir(dir){};
};

int M, S, ans=0;
int R=4, C=4;
int maxi=0, visited[R][C];
string min_str;
Fish shark;
vector<Fish> fishes;
vector<int> kill_list;
vector<vector<vector<int>>> graph;
vector<vector<vector<int>>> cpy;
vector<vector<int>> reek;
int xmoves[8] = {0, -1, -1, -1, 0, 1, 1, 1};
int ymoves[8] = {-1, -1, 0, 1, 1, 1, 0, -1};
int xs[4] = {-1,0,1,0}; //shark moves 상좌하우
int ys[4] = {0,-1,0,1};

void getInput(){
    int x, y, dir;
    cin >> M >> S;
    for (int i=0; i<M; i++) {
        cin >> x >> y >> dir;
        fishes.push_back(Fish(i+1,x-1,y-1,dir-1));
        graph[x][y].push_back(i+1);
    }
    cin >> shark.x >> shark.y;
    shark.x-=1;
    shark.y-=1;
}

bool canGo(int x, int y){
    if (x < 0 || x >= R || y <0 || y>=C) return false;
    return true;
}

void mv_fishes(int step){
    for (auto& fish: fishes) {
        int cx=fish.x, cy=fish.y, dir=fish.dir;
        int dx=xmoves[dir], dy=ymoves[dir];
        int nx=cx+dx, ny=cy+dy;
        if (dir == -1) {
            // 먹힌 물고기
            continue;
        }

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
    }
}

void mv_shark(int step){
    maxi = 0;
    min_str = "999";

    memset(visited, 0, sizeof(visited));
    kill_list.clear();
    search(shark.x, shark.y, {}, "");
    // 물고기 죽이기
    for (auto& fish_nr:kill_list) {
        Fish fish = fishes[fish_nr-1];
        int nr, x, y;
        nr = fish.nr, x = fish.x, y = fish.y;
        graph[x][y].clear(); // 생선 지우기
        fish.dir = -1;
        reek[x][y] = step; // 현재 스텝의 냄새 남김
    }

}


void search(int cx, int cy, vector<int>& dead_fish, string dirs){
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
            for (int fish_nr:graph[nx][ny]){
                dead_fish.push_back(fish_nr);
            }
            search(nx,ny, dead_fish, dirs+to_string(i+1)); // std::to_string
            visited[nx][ny]=0;
            for (int n=0; n<graph[nx][ny].size(); n++) {
                dead_fish.pop_back();
            }
        }
    }
}

void run_step(int step){


    mv_fishes(step);
    mv_shark(step);

    for (int r=0; r<R; r++) {
        for (int c=0; c<C; c++) {
            for (int nr:cpy[r][c]){
                
            }
        }
    }

}