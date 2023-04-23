import sys; readl = sys.stdin.readline

N = int(readl())
graph = [[0] * N for _ in range(N)]
group = [[0] * N for _ in range(N)]
for i in range(N):
    row = list(map(int, readl().split()))
    for j in range(N):
        graph[i][j] = int(row[j])

moves = [(0,1), (0,-1), (1,0), (-1,0)]
def dfs(r,c,v):
    if r < 0 or r >= N or c <0 or c >= N:
        return False
    if group[r][c] != 0:
        return False
    group[r][c] = v # 색칠
    for dr, dc in moves:
        nr, nc = r+dr, c+dc
        dfs(nr,nc,v)
        
def seg(x,y,d1,d2):
    # 5
    for i in range(0, d1+1):
        if 0 <= x+i < N and 0 <= y-i < N: 
            group[x+i][y-i] = 5
        if 0 <= x+d2+i < N and 0 <= y+d2-i < N: 
            group[x+d2+i][y+d2-i] = 5
    for i in range(0, d2+1):
        if 0 <= x+i < N and 0 <= y+i < N: 
            group[x+i][y+i] = 5
        if 0 <= x+d1+i < N and 0 <= y-d1+i < N: 
            group[x+d1+i][y-d1+i] = 5
    
    # 1번 기준으로
    for r in range(x-1, -1, -1):
        group[r][y] = 1;
    # 2
    for c in range(y+d2+1, N):
        group[x+d2][c] = 2
    for c in range(y-d1-1, -1, -1):
        group[x+d1][c] = 3
    for r in range(x+d1+d2+1, N):
        group[r][y-d1+d2] = 4
    
    dfs(0,0,1) # 1번
    dfs(0,N-1,2)
    dfs(N-1,0,3)
    dfs(N-1,N-1,4)
    
    counts = [0] * 6 
    for i in range(N):
        for j in range(N):
            counts[group[i][j]] += graph[i][j]
    counts[5] += counts[0]
    
    mini, maxi = float("inf"), -float("inf")
    for i in range(1,6):
        mini = min(mini, counts[i])
        maxi = max(maxi, counts[i])
    return maxi - mini
ans = float("inf")
for x in range(0, N-3+1):
    for y in range(1, N-2+1):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x+d1+d2 > N:
                    continue
                if y-d1 < 1:
                    continue
                if y+d2 > N or y+d2 <= y:
                    continue
                ans = min(ans, seg(x,y,d1,d2))
print(ans)        
        
        