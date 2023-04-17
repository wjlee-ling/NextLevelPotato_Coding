import sys; readl = sys.stdin.readline
graphs = [list(readl().strip()) for _ in range(4)]
n_rot = int(readl())

def bfs(idx, heading):
    def rotate(idx, clock):
    # clock: 1: clock-wise, -1: counter-clock-wise
        if clock==1:
            graphs[idx] = [graphs[idx][-1]] + graphs[idx][:-1]
        else:
            graphs[idx] = graphs[idx][1:] + [graphs[idx][0]] 
    visited[idx] = 1
    rotate(idx, heading)
    for dx in [1,-1]:
        if idx+dx>=0 and idx+dx<4 and not visited[idx+dx]:
            if dx == 1 and polarity[idx]:
                bfs(idx+dx, -heading)
            elif dx == -1 and polarity[idx-1]:
                bfs(idx+dx, -heading) 

def check_polarity():
    results = [] # [0-1, 1-2, 2-3]
    for i in range(3):
        results.append(graphs[i][2] != graphs[i+1][-2])
    return results    

for _ in range(n_rot):
    visited = [0,0,0,0]
    idx, heading = map(int, readl().split())
    polarity = check_polarity()
    bfs(idx-1, heading)
    #print(graphs)
            
ans = 0
for i in range(1, 5):
    score = 2**(i-1)
    if graphs[i-1][0] == "1":
        ans += score

print(ans)
    