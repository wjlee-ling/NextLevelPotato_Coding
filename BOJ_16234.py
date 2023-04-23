from collections import deque
import sys; readl = sys.stdin.readline
N, L, R = map(int, readl().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, readl().split())))

def bfs(x,y):
    moves = [(1,0),(0,1),(-1,0),(0,-1)]
    q = deque([(x,y)])
    union = set([(x,y)])
    cumsum = 0
    while q:
        cx, cy = q.popleft()
        cumsum += graph[cx][cy]
        for dx, dy in moves:
            nx, ny = cx+dx, cy+dy
            if 0<=nx<N and 0<=ny<N and L <= abs(graph[nx][ny] - graph[cx][cy]) <= R and (nx,ny) not in union:
                q.append((nx,ny))
                union.add((nx,ny))
    return union, cumsum

def run(days=0):
    flag = 0
    visited_on_day = set()
    changes = []
    for i in range(N):
        for j in range(N):
            if (i,j) in visited_on_day:
                continue
            union, cumsum = bfs(i,j)
            visited_on_day = visited_on_day.union(union)
            if len(union) >1:
                changes.append((cumsum, union))
                if flag == 0:
                    days += 1
                flag = 1

    for (cumsum, pairs) in changes:
        for pair in pairs:
            graph[pair[0]][pair[1]] = cumsum // len(pairs)

    if flag:
        return run(days)
    else:
        print(days)
        return ;

run()