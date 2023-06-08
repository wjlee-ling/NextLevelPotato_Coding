#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int N, M, K, origin_x, origin_y;
vector<int> dice = {0, 0, 0, 0, 0, 0};
vector<vector<int>> graph;
int xmoves[] = {0,0,0,-1,1};
int ymoves[] = {0,1,-1,0,0};


void roll(int num){
    int a,b,c,d;
    if (num == 1) {
        // {2, 4, 1, 3, 5, 6} => {2, 6, 4, 1, 5, 3}
        a = dice[1], b = dice[2], c = dice[3], d = dice[5]; // 
        dice[1] = d, dice[2] = a, dice[3] = b, dice[5] = c; // dice[1] = dice[5]
    } else if (num == 2) {
        // {2, 4, 1, 3, 5, 6} => {2, 1, 3, 6, 5, 4}
        a = dice[1], b = dice[2], c = dice[3], d = dice[5];
        dice[1] = b, dice[2] = c, dice[3] = d, dice[5] = a;
    } else if (num == 3) {
        // {2, 4, 1, 3, 5, 6} => {1, 4, 5, 3, 6, 2}
        a = dice[0], b = dice[2], c = dice[4], d = dice[5];
        dice[0] = b, dice[2] = c, dice[4] = d, dice[5] = a;
    } else {
        a = dice[0], b = dice[2], c = dice[4], d = dice[5];
        dice[0] = d, dice[2] = a, dice[4] = b, dice[5] = c; 
    }
}

void check_dice() {
    cout << dice[0] << dice[1] << dice[2] << dice[3] << dice[4] << dice[5] << endl;
}

void check_map(){
    for (int n=0; n<N; n++) {
        for (int m=0; m<M; m++){
            cout << graph[n][m];
        }
        cout << "" << endl;
    }
}

vector<int> run_step(int num, int x, int y) {
    roll(num);
    // cout << "after rolling: " <<  dice[0] << dice[1] << dice[2] << dice[3] << dice[4] << dice[5] << endl;
    if (graph[x][y] == 0){
        graph[x][y] = dice[5];
    } else {
        dice[5] = graph[x][y];
        graph[x][y] = 0;
    }
    cout << dice[2] << endl;
    // check_dice();
    // check_map();
    return dice;
}

int main(){
    int cx, cy;
    cin >> N >> M >> origin_x >> origin_y >> K;
    graph.resize(N, vector<int>(M, 0));
    for (int n=0; n<N; n++) {
        for (int m=0; m<M; m++){
            cin >> graph[n][m];
        }
    }
    cx = origin_x;
    cy = origin_y;
    for (int k=0; k<K; k++){
        int num, nx, ny;
        cin >> num;
        nx = cx + xmoves[num];
        ny = cy + ymoves[num];
        if (! (0 <= nx && nx < N && 0 <= ny && ny <M)) {
            continue;
        } 
        dice = run_step(num, nx, ny);
        cx = nx, cy = ny;
    }
    //

    return 0;
}