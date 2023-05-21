from collections import deque
moves = [(0,1), (1,0), (0,-1), (-1,0)] # E, S, W, N 
heading = []
def redir(h):
    if h == 0: #E
        return 2
    elif h == 1:#S
        return 3
    elif h == 2: #W
        return 0
    else: #N
        return 1

def compare(h, bottom, score):
    if bottom > score:
        return (h+1)%4
    elif bottom < score:
        return (h-1)%4
    else:
        return h
    
def turn_dice(faces, h):
    if h == 0 :
        faces[1], faces[2], faces[3], faces[5] = faces[5], faces[1], faces[2], faces[3]
    elif h == 1:
        faces[0], faces[2], faces[4], faces[5] = faces[5], faces[0],faces[2], faces[4]
    elif h == 2:
        faces[1], faces[2], faces[3], faces[5] = faces[2], faces[3], faces[5], faces[1]
    else:
        faces[0], faces[2], faces[4], faces[5] = faces[2],faces[4],faces[5], faces[0]
    return faces

N, M, K = map(int, input().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))
ans, h = 0, 0
curr = (0,0) # start
faces = [2,4,1,3,5,6]
while K>0:
    cx, cy = curr
    dx, dy = moves[h]
    nx, ny = cx+dx, cy+dy
    if 0 > nx or nx >= N or 0 > ny or ny >=M:
        h = redir(h)
        continue
    faces = turn_dice(faces, h)
    score = graph[nx][ny]
    bottom = faces[-1]
    h = compare(h, bottom, score)
    q = deque([(nx,ny)]) 
    hist = [[1] * M for _ in range(N)] 
    hist[nx][ny] = 0
    while q:
        qcx, qcy = q.popleft()
        ans += score
        for (dx,dy) in moves:
            qnx, qny = qcx+dx, qcy+dy
            if 0<=qnx<N and 0<=qny<M and hist[qnx][qny] and graph[qnx][qny]== score:
                hist[qnx][qny] = 0
                q.append((qnx,qny))
    curr = (nx,ny)
    K -=1

print(ans)