import sys; readl = sys.stdin.readline
from collections import deque
N, M, g = map(int, readl().strip().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, readl().strip().split())))
x, y = map(lambda x: int(x)-1, readl().strip().split())
starts, dests = dict(), dict()
for num in range(M):
    a,b,c,d = map(int, readl().strip().split())
    starts[(a-1,b-1)] = num+1 # to avoid label 0
    dests[num+1] = (c-1,d-1)

# move taxi
moves = [(-1,0),(0,-1),(0,1),(1,0)] ## 같은 거에 행이 적거나 열이 적은 거  우ㄴ
def cal_dist(cx,cy,nx,ny):
    # get distance b/w passenger and his destination
    return abs(nx-cx) + abs(ny-cy)
    

def mv_taxi(x, y, gas):
    # print(x,y,gas)
    if gas < 0:
        return -1
    if len(starts) == 0: return gas
    q = deque([(x,y,0)])
    visited = [[1]*N for _ in range(N)]
    visited[x][y] = 0
    ret = -1
    while q:
        cx, cy, cs = q.popleft()
        # print(f"cx: {cx} cy: {cy} rest: {gas-cs}")
        next_ls = [] # candidates for next ride
        for dx, dy in moves:
            nx,ny = cx+dx, cy+dy
            # go to get client
            if 0<=nx<N and 0<=ny<N and graph[nx][ny]==0 and visited[nx][ny]:
                visited[nx][ny] = 0 # visited
                q.append((nx,ny, cs+1))
                
                if starts.get((nx,ny), 0):
                    next_ls.append((nx,ny,cs+1))
                    
        if next_ls:
            # find closest passenger
            cx,cy,cs = sorted(next_ls, key=lambda x: (x[2], x[0], x[1]))[0]
            gas -= cs
            if gas <= 0: return -1;
        
            taxi_num = starts[(cx,cy)]
            del starts[(cx,cy)]
            dest_x, dest_y = dests[taxi_num]
            # go to his destination
            q2 = deque([(cx,cy,0)])
            visited = [[1]*N for _ in range(N)]
            visited[cx][cy] = 0
            while q2:
                cx, cy, cs = q2.popleft()
                if cx == dest_x and cy == dest_y:
                    if gas-cs < 0: return -1
                    ret = mv_taxi(dest_x, dest_y, gas+cs)
                    return ret
                for dx, dy in moves:
                    nx,ny = cx+dx, cy+dy
                    # go to destination
                    if 0<=nx<N and 0<=ny<N and graph[nx][ny]==0 and visited[nx][ny]:
                        visited[nx][ny] = 0 # visited
                        if gas-cs-1 < 0:
                            # run out of gas on the way to pick up passenger
                            return -1
                        q2.append((nx,ny, cs+1))

    return ret

ret = mv_taxi(x,y,g)
print(ret)