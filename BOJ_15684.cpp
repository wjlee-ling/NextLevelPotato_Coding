#include<iostream>

int n, m, h, ret; // 세로, 가로, 세로선 위 위치, return 여부
int map[31][11];

bool check() {
    bool ret = true;

    for (int i = 1; i <=n; ++i){
        // columnwise
        int pos = i;

        for (int j = 0; j <= h; ++j) {
            // row-wise
            if (map[j][pos] == 1) { // 오른쪽
                ++pos;
            }
            else if (map[j][pos-1] == 1) { // 왼쪽
                --pos;
            }
        }

        if (pos != i) {
            // 돌아오지 않으면
            return ret = false;
        }
    }

    return ret;
}

void dfs(int count, int y, int x) {
    if (count >= ret) return ;
    if (check()) {
        ret = count;
        return;
    }
    if (count == 3) return ;
    for (int c = y; c <= h; ++c) {
        for (int r = x; r < n; ++r) {
            if (map[c][r] == 0 && map[c][r-1] == 0 && map[c][r+1]==0) {
                map[c][r] = 1;
                dfs(count+1, c, r);
                map[c][r] = 0;
            }
        }
        x = 1;
    }
}

int main()
{
    std::cin >> n >> m >> h;
    int a, b; 
    for (int i = 0; i < m; ++i) {
        std::cin >> a >> b;
        map[a][b] = 1;
    }

    ret = 4;
    dfs(0, 1, 1);
    if (ret == 4) ret = -1;
    std::cout << ret ;  
    return 0;
}