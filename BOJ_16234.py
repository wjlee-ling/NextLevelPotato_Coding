"""
visited를 set이 아닌 global graph로 처리하니까 시간 초과 통과
"""

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
            if 0<=nx<N and 0<=ny<N and L <= abs(graph[nx][ny] - graph[cx][cy]) <= R and visited[nx][ny] == False:
                q.append((nx,ny))
                union.add((nx,ny))
                visited[nx][ny] = True
                
    if len(union) > 1:
        for nx,ny in union:
            graph[nx][ny] = cumsum // len(union)
        return True;

    return False
days=0
while True:
    visited = [[False] * N for _ in range(N)]
    flag = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == False:
                visited[i][j] = True
                if bfs(i,j):
                    flag = 1
    if flag == 0:
        break
    days += 1

print(days)

