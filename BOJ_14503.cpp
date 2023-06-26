#include <vector>
#include <iostream>
#include <algorithm>
#include <queue>

using namespace std;

int N, M, start_x, start_y, d;
int xmoves[] = {-1,0,1,0};
int ymoves[] = {0,1,0,-1};
int ans = 0;
vector<vector<int>> grid;

bool isValid(int cx, int cy){
    return (0 <= cx && cx < N && 0 <= cy && cy < M && grid[cx][cy] != 1);
}

int reverse(int cx, int cy, int dir){
    return (dir==0) ? 2 : (dir==1) ? 3 : (dir==2) ? 0 :  1;
}

void step(int x, int y, int dir){
    queue<pair<int,int>> q;
    while (! q.empty()){
        x = q.front().first;
        y = q.front().second;
        q.pop();
        if (grid[x][y] == 0){
            // cleaning
            grid[x][y] = 2;
            ans ++;
        }
        int nx, ny;
        for (int i=0; i<4; i++){
            int new_dir;
            new_dir = dir - i; 
            if (new_dir <0 ) new_dir = 3;
            
            nx = x + xmoves[new_dir];
            ny = y + ymoves[new_dir];
            if (grid[nx][ny] == 0) {
                q.push(pair(nx,ny));
                break;
            }
        }
        // 후진
        nx = x - xmoves[dir];
        ny = y - ymoves[dir];
        if (isValid(nx,ny)){
            q.push(pair(nx,ny));
        } else {
            break;
        } 
    }
}

int main(){
    cin >> N >> M;
    cin >> start_x >> start_y >> d;
    grid.resize(N, vector<int>(M, 0));
    for (int r = 0; r < N; r++){
        for (int c = 0; c < M; c++){
            cin >> grid[r][c];
        }
    }
    step(start_x, start_y, d);
    cout << ans;
}

