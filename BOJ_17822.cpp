#include <vector>
#include <iostream>
using namespace std;

int N, M, T, X, D, K, ans=0;
vector<vector<int>> graph(49, vector<int>(49));
vector<vector<int>> seen(49, vector<int>(49));

void rotate(int idx, int d, int k){
    if (d == 0) {
        while (k>0){
            graph[idx].insert(graph[idx].begin(), graph[idx][M-1]);
            k--;
        }
    }
    else if (d == 1) {
        while (k>0) {
        int first = graph[idx].front();
        graph[idx].erase(graph[idx].begin());
        graph[idx].push_back(first); 
        k--;
        }
    }
}

void remove_dup(int i, int j){
    if (i == N-1 || j >= M || j <0) return ;
    if (seen[i][j]) return ;
    seen[i][j] = true;
    if (i < N-1 && graph[i][j] == graph[i+1][j]) {
        remove_dup(i+1, j);
    }
    if (j <= M-2  && graph[i][j] == graph[i][j+1]) {
        remove_dup(i, j+1);
    }
    else if (j == M-1 && graph[i][j] == graph[i][0]) {
        remove_dup(i, 0);
    }
    else {
        ans += graph[i][j];
        return ;
    } 
    graph[i][j] = 0;
    return ;
}


int main() {
    cin >> N >> M >> T;
        
    for (int i=0; i<N; i++) {
        for (int j=0; j<M; j++) {
            int ele;
            cin >> ele;
            graph[i][j] = ele;
        }
    }
    for (int t=0; t<T; t++){
        cin >> X >> D >> K;
        for (int x=X; x<N+1; x+=X) {
            rotate(x-1, D, K);
        }
    }
    for (int i=0; i<N; i++){
        for (int j=0; j<M; j++) {
            remove_dup(i,j);
        }
    }
    cout << ans;
    return 0;
}