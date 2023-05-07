from collections import defaultdict
from copy import deepcopy

moves = {1: (-1,0), 2:(-1,-1), 3:(0,-1), 4:(1,-1), 5:(1,0), 6:(1,1), 7: (0,1), 8:(-1,1)}
graph = [[0]*4 for _ in range(4)]
heading = defaultdict(int) # ith: heading, -1 == shark
coord = defaultdict(tuple) 

for i in range(4):
    ls = list(map(int, input().split()))
    for j in range(4):
        a, b = ls[2*j], ls[2*j+1]
        heading[a] = b
        coord[a] = (i,j)
        graph[i][j] = a

def move_fish(heading, coord):
    for n in range(1, 17):
        if heading[n] == 0:
            # 잡아먹힘
            continue
        (cx, cy) = coord[n]
        dx, dy = moves[heading[n]]
        nx, ny = cx+dx, cy+dy
        # rotate
        while nx < 0 or ny <0 or nx>=4 or ny>=4 or graph[nx][ny] == -1 :
            heading[n] = (heading[n]+1) % 8 if heading[n] != 7 else 8
            dx, dy = moves[heading[n]]
            nx, ny = cx+dx, cy+dy
        # swap w/ another fish
        swap_n = graph[nx][ny]
        graph[cx][cy], graph[nx][ny] = graph[nx][ny], graph[cx][cy]
        coord[n], coord[swap_n] =  (nx,ny), (cx,cy) # coord[swap_n], coord[n]
        
        
def move_shark(x, y, cumsum, heading, coord):
    global ans
    move_fish(heading, coord)
    graph[x][y] = 0 # 상어가 떠남
    dx, dy = moves[heading[-1]] # 상어 현재 방향
    flag,scale = 1, 1
    nx,ny = x+scale*dx, y+scale*dy
    while nx <= 3 and ny <= 3 and graph[nx][ny] >= 1:
        if graph[nx][ny] == 0:
            continue
        flag = 0
        # shark eating fish
        fish = graph[nx][ny]
        graph[nx][ny] = -1
        
        newcoord = deepcopy(coord)
        newcoord[-1] = (nx,ny)
        
        newheading = deepcopy(heading)
        newheading[-1] = newheading[fish]
        newheading[fish] = 0
        
        move_shark(nx, ny, cumsum+fish, newheading, newcoord)
        # backtrack
        graph[nx][ny] = fish
        
        scale += 1
        nx,ny = x+scale*dx, y+scale*dy
    
    if flag: # 갈 데 없음
        ans = max(ans, cumsum)
        
ans = 0
start = graph[0][0]
heading[-1] = heading[start]
heading[start] = 0
coord[-1] = (0,0)
graph[0][0] = -1

move_shark(0, 0, start, heading, coord)
# 언제 move_fish?
print(ans)