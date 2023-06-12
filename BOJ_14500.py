N, M = map(int, input().split())
graph = []
seen = [[0]*M for _ in range(N)]
for _ in range(N):
    graph.append(list(map(int, input().split())))

xmoves = [-1,0,1,0] # N, E, S, W
ymoves = [0,1,0,-1]

ans = 0
def is_valid(nx, ny):
    global N, M
    return (0<=nx<N and 0<=ny<M)


def pattern1(cx, cy, dir, step, cumsum):
    global ans
    dirs = {-1: [0,1,2,3], 0: [0,1,3], 1:[0,1,2], 2:[1,2,3], 3:[0,2,3]}
    cumsum += graph[cx][cy]
    if step==4:
        ans = max(cumsum, ans)
        return

    for new_dir in dirs[dir]:
        nx = cx + xmoves[new_dir]
        ny = cy + ymoves[new_dir]
        if is_valid(nx,ny) and seen[nx][ny] == 0:
            seen[nx][ny] = 1
            pattern1(nx, ny, new_dir, step+1, cumsum)
            seen[nx][ny] = 0

def pattern2(cx, cy):
    global N, M, ans
        # 뻐큐모양
    patterns = [
        [(0,1), (0,2), (-1,1)], # 가로 위
        [(0,1), (0,2), (1,1)], # 가로 아래
        [(1,0), (2,0), (1,1)], # 세로 오른쪽
        [(1,0), (2,0), (1,-1)], # 세로 왼쪽
    ]
    maxi = 0
    for pattern in patterns:
        cumsum = graph[cx][cy]
        flag = 0
        for (dx,dy) in pattern:
            nx = cx + dx
            ny = cy + dy
            if not is_valid(nx,ny):
                flag = 1
                break
            cumsum += graph[nx][ny]
        if flag == 1:
            continue
        maxi = max(maxi, cumsum)
    ans = max(maxi, ans)

for x in range(N):
    for y in range(M):
        seen[x][y] = 1
        pattern1(x,y,-1,1,0)
        seen[x][y] = 0
        pattern2(x,y)    
print(ans)