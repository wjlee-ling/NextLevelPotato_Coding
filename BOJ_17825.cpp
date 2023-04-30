#include <vector>
#include <iostream>
#include <unordered_map>
#include <algorithm>

using namespace std;
vector<int> dice;
vector<int> pieces(4, 0);
unordered_map<int, vector<int>> graph;

int idx=0, m=0, cumsum=0, ans=0; //

// no detour from 30
void move(int idx, int m, int cumsum){
    // idx= idx of rolling dice, m = map idx
    if (idx >= 10) {
        ans = max(ans, cumsum);
        return ;
    } 
    for (int pidx=0; pidx<4; pidx++) {
        int newpos, oldpos, face = dice[idx];
        oldpos = pieces[pidx];
        if (oldpos > 40) {
            continue;
        } 
        if (m == 0) newpos = oldpos+2*face;
        else if (m == 1) {
            int oldidx = distance(graph[10].begin(), find(graph[10].begin(), graph[10].end(), oldpos));
            newpos = graph[10][oldidx+face];
        }
        else if (m == 2) {
            int oldidx = distance(graph[20].begin(), find(graph[20].begin(), graph[20].end(), oldpos));
            newpos = graph[20][oldidx+face];
        }
        if (newpos <= 40) {
            if (find(pieces.begin(), pieces.end(), newpos) != pieces.end()) {
                continue;
            }
            cumsum += newpos;
            pieces[pidx] = newpos;
        } else {
            pieces[pidx] = newpos; // eixt -> no adding up
        }

        if (newpos==10){
            move(idx+1, 1, cumsum);
        }
        else if (newpos==20) {
            move(idx+1, 2, cumsum);
        }
        else move(idx+1, m, cumsum);
        pieces[pidx] = oldpos;
        if (newpos <=40) cumsum -= newpos;
    }
    
}

int main() {
    for (int i=0; i<10; i++) {
        int num;
        cin >> num;
        dice.push_back(num);
    }
    graph[10] = vector<int>({10, 13, 16, 19, 25, 30, 35, 40});
    graph[20] = vector<int>({20, 22, 24, 25, 30, 35, 40});
    move(idx, m, cumsum);
    
    cout << ans;
}