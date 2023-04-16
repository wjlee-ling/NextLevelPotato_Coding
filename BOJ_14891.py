import sys; readl = sys.stdin.readline
graphs = [list(readl().strip()) for _ in range(4)]
n_rot = int(readl())

def bfs(idx, heading):
    def rotate(idx, clock):
    # clock: 1: clock-wise, 0: counter-clock-wise
        if clock==1:
            graphs[idx] = [graphs[idx][-1]] + graphs[idx][:-1]
        else:
            graphs[idx] = graphs[idx][1:] + [graphs[idx][0]]
    visited[idx] = 1
    rotate(idx, heading)
    for dx in [1,-1]:
        if idx+dx>=0 and idx+dx<4 and not visited[idx+dx] and graphs[idx][2*dx] != graphs[idx+dx][-2*dx]:
            bfs(idx+dx, -heading) 
            
for _ in range(n_rot):
    visited = [0,0,0,0]
    idx, heading = map(int, readl().split())
    idx -= 1
    bfs(idx, heading)
            
ans = 0
print(graphs)
for i in range(1, 5):
    score = 2**(i-1)
    if graphs[i-1][0] == "1":
        ans += score

print(ans)
    