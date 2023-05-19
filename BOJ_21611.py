N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
magics = [tuple(map(int, input().split())) for _ in range(M)]
 
 
n2loc = {} 
loc2n = {} 
n2ball = [-1] * N**2 # ㄱ구슬 번호
result = 0
 
 
def init_grid():

    global n2loc, loc2n
 
    dy_temp = (0, 1, 0, -1)
    dx_temp = (1, 0, -1, 0)
 
    loc = (0, -1) # 시작을 (0, -1)
    cnt = N ** 2 - 1
    dist, flag = N, 1 
    dir = 0
 
    while True:
        for i in range(dist):
            ny = loc[0] + dy_temp[dir]
            nx = loc[1] + dx_temp[dir]
 
            loc = (ny, nx) 
            n2loc[cnt] = (ny, nx)
            loc2n[(ny, nx)] = cnt
            n2ball[cnt] = board[ny][nx]
            cnt -= 1
        dir = (dir + 1) % 4
        flag += 1
        if flag == 2: 
            flag = 0
            dist -= 1
 
        if dist == 0: break 
 
def remap():
    global n2ball
    del_cnt = n2ball.count(-1)
    n2ball = [ball for ball in n2ball if ball != -1]
    n2ball.extend([0]*del_cnt)
 
def destroy(d, s):
    dy = (0, -1, 1, 0, 0)
    dx = (0, 0, 0, -1, 1)
 
    shark_loc = (int(N / 2), int(N / 2))
    y, x = shark_loc
    for i in range(1, s+1, 1):
        ny = y + dy[d] * i
        nx = x + dx[d] * i
 
        n = loc2n[(ny, nx)] 
        n2ball[n]=-1 
 
def destroy2():
    global result
    ret = False
 
    cnt = 0
    target = 0
    ball_num = 0
 
    for i in range(N**2):
        if n2ball[i] == n2ball[target]: # 연속
            cnt+=1 
        else:
            if cnt >= 4:
                ret = True
                for n in range(target, i, 1):
                    n2ball[n] = -1
                result += ball_num * cnt 
            cnt = 1
            target = i
            ball_num = n2ball[i]
 
    return ret # True or False 반환
 
def regroup():
    global n2ball
    new_n2ball = [0]
    group = [] 
    for n in range(1, N**2, 1):
        if not group: group.append(n2ball[n])
        elif n2ball[n] == group[0]:
            group.append(n2ball[n])
        else:
            new_n2ball.append(len(group)) 
            new_n2ball.append(group[0]) 
            group = [n2ball[n]] 
 
    n2ball = [0] * N ** 2 
    for i in range(len(new_n2ball)):
        if i >= (N ** 2): break
        n2ball[i] = new_n2ball[i]
 
def solve():
    init_grid()
    for d, s in magics:
        destroy(d, s)
        remap()
        while True:
            if not destroy2(): break
            remap()
        regroup()
 
solve()
print(result)