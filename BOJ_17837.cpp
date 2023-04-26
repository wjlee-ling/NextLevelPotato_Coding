#include<iostream>
#include<vector>
#include<algorithm>

#define MAX 12
#define CHESS_MAX 10

using namespace std;

struct CHESS {
    int x;
    int y;
    int dir;
};

int N, K, ans;
int map[MAX][MAX];
vector<int> states[MAX][MAX];
CHESS chess[CHESS_MAX];

int dx[5] = {0, 0, 0, -1, 1};
int dy[5] = {0, 1, -1, 0, 0};

void input() {
    cin >> N >> K ;
    for (int i=0; i < N; i++) {
        for (int j=0; j < N; j++) {
            cin >> map[i][j];
        }
    }

    for (int i=0; i < K; i++) {
        int x, y, d; 
        cin >> x >> y >> d;
        x--; y--;
        chess[i] = {x,y,d};
        states[x][y].push_back(i);
    }
}

int find_idx(int x, int y, int chess_num) {
    // 지울 장기 번
    auto it = find(states[x][y].begin(), states[x][y].end(), chess_num);
    return distance(states[x][y].begin(), it);
}

int reverse_dir(int num) {
    int dir = chess[num].dir;
    return (dir == 1) ? 2 : (dir == 2) ? 1 : (dir == 3) ? 4 : 3;
}

void move(int x, int y, int nx, int ny, int num, int idx, int st) {
    if (st == 0) {
        for (int i = idx; i < states[x][y].size(); i++) {
            states[nx][ny].push_back(states[x][y][i]);
            chess[states[x][y][i]].x = nx;
            chess[states[x][y][i]].y = ny;
        }
        states[x][y].resize(idx); // states[x][y] = vector<int>(states[x][y].begin(), states[x][y].begin()+idx);
    }

    else if (st == 1) {
        for (int i = states[x][y].size()-1; i>= idx; i--)
        {
            states[nx][ny].push_back(states[x][y][i]);
            chess[states[x][y][i]].x = nx;
            chess[states[x][y][i]].y = ny;
        }
        states[x][y].resize(idx); // states[x][y] = vector<int>(states[x][y].begin(), states[x][y].begin()+idx);
    }

    else if (st == 2)
    {
        int dir = reverse_dir(num);
        chess[num].dir = dir;
        int nx = x + dx[dir];
        int ny = y + dy[dir];
        if (nx >= 0 && ny >= 0 && nx < N && ny < N) {
            if (map[nx][ny] != 2) move(x, y, nx, ny, num, idx, map[nx][ny]);
        }
    }
}

bool check_states(){
    for (int i = 0; i < K; i++) {
        int x = chess[i].x;
        int y = chess[i].y;
        if (states[x][y].size() >= 4) return true;
    }
    return false;
}

void solution() {
    bool flag = false;
    int steps = 0;
    while (true) {
        if (steps > 1000) break;
        for (int i = 0; i < K; i++) {
            int x = chess[i].x;
            int y = chess[i].y;
            int dir = chess[i].dir;

            int nx = x + dx[dir];
            int ny = y + dy[dir];

            int idx = find_idx(x, y, i);
            
            if (nx >= 0 && nx < N && ny >= 0 && ny < N) {
                move(x,y,nx,ny,i,idx,map[nx][ny]);
            }
            else move(x,y,nx,ny,i,idx,2); // blue
            if (check_states() == true) {
                flag = true;
                break;
            }
        }
        if (flag == true) break;
        steps ++;
    }
    if (flag == true) cout << steps +1 << endl;
    else cout << -1 << endl;
}

int main(){
    input();
    solution();
    return 0;
}