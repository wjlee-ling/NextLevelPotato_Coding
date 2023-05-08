#include <iostream>
#include <vector>

using namespace std;

struct Fish{
    int y, x, d, n;
    Fish(int y, int x, int d, int n): y(y), x(x), d(d), n(n){}
};

const int dy[]={-1,-1,0,1,1,1,0,-1};
const int dx[]={0,-1,-1,-1,0,1,1,1};

bool inRange(int y, int x){
    return y>=0 && x >=0 && y <4 && x<4;
}

int solve(int y, int x, vector<vector<int>> graph, vector<Fish> fishes) {
    int ret, d;
    Fish& eaten = fishes[graph[y][x]];

    d=eaten.d;
    ret=eaten.n;

    eaten.d=-1;
    graph[y][x]=-1;

    for (Fish& f:fishes) {
        if (f.d==-1) continue; // eaten
        bool flag=false;
        int ny, nx, fd = f.d;

        while(true) {
            ny=f.y+dy[f.d];
            nx=f.x+dx[f.d];
            if (inRange(ny,nx)&&(ny!=y||nx!=x)) break;
            if (++f.d>7) f.d=0; // rotate
            if (f.d==fd) { // return to the first d
                flag=true;
                break;
            }
        }
    if (flag) continue;
    if (graph[ny][nx]!=-1) { //swap
        fishes[graph[ny][nx]].y = f.y;
        fishes[graph[ny][nx]].x = f.x;
    }
    graph[f.y][f.x] = graph[ny][nx];
    graph[ny][nx] = f.n-1;
    f.y = ny;
    f.x = nx;
    }
    //backtracking
    int ny=y, nx=x;
    while (true) {
        ny+=dy[d];
        nx+=dx[d];

        if (!inRange(ny,nx)) break;
        if (graph[ny][nx]==-1) continue;
        ret = max(ret, eaten.n+solve(ny,nx,graph,fishes));
    }

    return ret;
}

int main(){
    vector<Fish> fishes(16, Fish(0,0,0,0));
    vector<vector<int>> graph(4, vector<int>(4));

    for (int i=0;i<4;i++) {
        for (int j=0;j<4;j++) {
            int n,d; cin >>n>>d;
            fishes[n-1].y=i;
            fishes[n-1].x=j;
            fishes[n-1].d=d-1;
            fishes[n-1].n=n;
            graph[i][j] =n-1;
        }
    }
    cout << solve(0,0,graph, fishes);

    return 0;
}