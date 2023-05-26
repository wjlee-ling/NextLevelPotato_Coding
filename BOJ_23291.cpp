#include <vector>
#include <deque>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;

int N, K;
vector<deque<int>> graph;

void add_fish(){
    deque<int>& row = graph[3];
    int mini = *min_element(row.begin(), row.end()); // * for dereferencing the returned iterator
    for (int idx=0; idx<row.size(); idx++){
        if (row[idx]==mini) row[idx]++;
    }
}

pair<int, int> getBlockShape(){
    // 최자하에서부터 블록 크기 재기
    pair<int, int> ret = {0,0};
    for (int r=3; r>=0; r--){
        for (int c=0; c<N; c++) {
            if (graph[r][c] != 0) {
                ret.first = 4-r;
                ret.second = c+1;
            }
        }
    }
    return ret;
}

void rotate90(int block_h, int block_w){
    unordered_map<int, deque<int>> mp; 
    for (int cidx=0; cidx<block_w; cidx++){
        deque<int> col;
        for (int ridx=0; ridx<block_h; ridx++){
            col.push_back(graph[3-ridx][0]); // 1열 마지막행에서 열부터 수집
            graph[3-ridx].pop_front();
        }
        mp[cidx] = col;
    }
    // 열을 행으로 바꿈
    for (int idx=0; idx<block_w; idx++){
        for (int i=0; i<mp[idx].size(); i++){
            graph[3-block_w+idx][i] = mp[idx][i];
        }
    }
}

void mvFish(){
    vector<vector<int>> temp;
    int xmoves[2] = {1,0};
    int ymoves[2] = {0,1};

    temp.resize(4, vector<int>(N));

    for (int r=0; r<4; r++){
        for (int c=0; c<N; c++){
            for (int i=0; i<2; i++){
                int nr = r + xmoves[i];
                int nc = c + ymoves[i];
                if (nr>=4 || nc >=N) continue;
                if (graph[r][c]==0 || graph[nr][nc]==0) continue;

                int diff = abs(graph[r][c]-graph[nr][nc]) / 5;
                if (graph[r][c] > graph[nr][nc]){
                    temp[r][c] -= diff;
                    temp[nr][nc] += diff;
                } else {
                    temp[r][c] += diff;
                    temp[nr][nc] -= diff;
                }

            }
        }
    }
    // apply diff
    for (int r=0; r<4; r++) {
        for (int c=0; c<N; c++){
            graph[r][c] += temp[r][c];
        }
    }
}

void doFirst(){
    graph[2].push_front(graph[3].front());
    graph[3].pop_front();
    
    // get block shape
    int block_h, block_w=0;
    while (true) {
        pair<int, int> ret = getBlockShape();
        block_h = ret.first, block_w = ret.second;

        // base case
        int base = find(graph[3].begin(), graph[3].end(), 0) - graph[3].begin() + 1;
        if (base-block_w <= block_h) break;

        rotate90(block_h, block_w);
    }

}

void flatten(){
    int block_h, block_w;
    pair<int, int> ret = getBlockShape();
    block_h = ret.first, block_w = ret.second;

    deque<int> q = {};
    for (int cidx=0; cidx<block_w; cidx++){
        for (int ridx=0; ridx<block_h; ridx++){
            q.push_back(graph[3-ridx].front());
            graph[3-ridx].pop_front();
        }
    }
    for (int i=0; i<N; i++) {
        if (graph[3][i] == 0) break;
        q.push_back(graph[3][i]); 
    }
    graph[3] = q;
}

void doSecond(){
    deque<int> q;
    // N/2
    for (int i=0; i<N/2; i++){
        graph[2][N/2-1-i] = graph[3].front();
        graph[3].pop_front();
    }
    // N/4
    for (int c=0; c<N/4; c++){
        for (int r=0; r<2; r++) {
            graph[r][N/4-1-c] = graph[3-r][c];
        }
    }
    for (int i=0; i<N/4; i++){
        graph[2].pop_front();
        graph[3].pop_front();
    }
}

int getDiff(){
    int mini, maxi;
    mini = *min_element(graph[3].begin(), graph[3].end());
    maxi = *max_element(graph[3].begin(), graph[3].end());
    return maxi-mini;
}

void check(){
    for (int c=0; c<N; c++) {
        cout << graph[3][c] << " ";
    }
    cout << "==========" << endl;
}

int main(){
    cin >> N >> K;
    int ans = 0;
    graph.resize(4, deque<int>(N)); // 최대 높이 4, b/c N == (N/4) * 4
    
    for (int n=0; n<N; n++){
        cin >> graph[3][n];
    }

    int diff = K+1;
    while (diff > K) {
        ans+=1;
        add_fish();
        doFirst();
        mvFish();
        flatten();

        doSecond();
        mvFish();
        flatten();
        // check();
        diff = getDiff();
    } 
    cout << ans;
    return 0;
}
