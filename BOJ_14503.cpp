#include <vector>
#include <iostream>
#include <algorithm>

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
    if (grid[x][y] == 0) {
        // 청소
        grid[x][y] = 2; // 청소
        ans ++;
    }
    int i = 1;
    int new_dir, nx, ny;
    while (i <= 4){
        new_dir = dir - i;
        if (new_dir < 0) new_dir = 3;

        nx = x + xmoves[new_dir];
        ny = y + ymoves[new_dir];

        if (grid[nx][ny] == 0) {
            // 청소 안된 곳이 있으면 
            step(nx, ny, new_dir);
            return ;
        }
        i++;
    }
    // 청소할 수 없어 후진
    new_dir = reverse(x, y, dir);
    nx = x + xmoves[new_dir];
    ny = y + ymoves[new_dir];
    if (isValid(nx, ny)){
        step(nx, ny, new_dir);
        return ;
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

