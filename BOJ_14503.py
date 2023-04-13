import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    row = list(map(int, sys.stdin.readline().split()))
    graph.append(row)

moves = [(-1, 0), (0,1), (1,0), (0,-1)] # move when heading N, E, S, W, respectively
q = deque([(r,c)]) # start

def look_around(x,y):
    # 청소할 공간이 있으면 True
    for dx, dy in moves:
        nx, ny = x+dx, y+dy
        if valid(nx,ny) and (nx,ny) not in cleaned:
            # 벽이 아니고 청소 필요
            return True
    return False

def valid(x,y):
    if x < 0 or y < 0 or x>=n or y>=m:
        return False
    if graph[x][y] == 1:
        # 벽
        return False
    return True

def change_heading(heading):
    # N -> W (0->3), S -> E (2 ->1)
    return heading-1 if (heading>=1) else 3

ans = 0
cleaned = set()
while q:
    x,y = q.popleft()
    if (x,y) not in cleaned:
        ans+=1
        cleaned.add((x,y)) # cleaned

    if look_around(x,y):
        # 청소할 면이 있으면
        d = change_heading(d) # 방향 반시계 구십도
        dx, dy = moves[d]
        nx, ny = x+dx, y+dy
        if valid(nx,ny) and (nx,ny) not in cleaned: # 청소할 수 있음
            q.append((nx,ny))
        
    else:
        # 청소 없음
        # 방향 유지, 한칸 후진
        dx, dy = map(lambda x: -x, moves[d]) 
        nx, ny = x+dx, y+dy
        if valid(nx,ny):
            q.append((nx,ny))
        else:
            # 후진 벽
            break # 종료 

print(ans)
        