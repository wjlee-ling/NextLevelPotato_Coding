from collections import deque
from copy import deepcopy
from itertools import chain
N, M = map(int, input().split())
graph = []
origins = []
zeros = 0
for i in range(N):
    row = list(map(int, input().split()))
    graph.append(row)
    for j in range(N):
        if row[j] == 2:
            origins.append((i,j))

def is_valid(x,y):
    if 0 > x or x >= N or y <0 or y >= N:
        return False
    if graph[x][y] in [1,2]:
        return False
    return True

ans = N * N
def bfs(step):
    global graph, ans
    temp = deepcopy(bfs)
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    if step == M:
        highest = max(chain(*graph))
        ans = min(ans, highest)
        return ;
    x, y = origins[step]
    q = deque([(x,y)])
    while q:
        cx, cy = q.popleft()
        for dx, dy in moves:
            nx, ny = cx+dx, cy+dy
            if is_valid(nx,ny):
                if graph[nx][ny] == 0:  
                    graph[nx][ny] = graph[cx][cy] +1 
                    q.append((nx,ny))
                else:
                    graph[nx][ny] = min(graph[nx][ny], graph[cx][cy]+1)
                    if graph[nx][ny] == graph[cx][cy]+1:
                        q.append((nx,ny))
                
    bfs(step+1)
    # backtracking
    graph = deepcopy(temp)
    bfs(step+1)
    
bfs(0)
print(ans-2)
            
