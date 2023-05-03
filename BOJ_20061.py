N = int(input())
# graph
graph = [[0]*10 for _ in range(10)]
ans = 0
def can_move(nx,ny):
    if nx >= len(graph) or ny >= len(graph[0]) or graph[nx][ny] != 0:
        return False
    return True
            
def pop_row(x,y):
    global ans
    if graph[x][0] == graph[x][1] == graph[x][2] == graph[x][3] == 1:
        ans += 1
        graph[x][0] = graph[x][1] = graph[x][2] = graph[x][3] = 0

def pop_col(x,y):
    global ans
    if graph[0][y] == graph[1][y] == graph[2][y] == graph[3][y] == 1:
        ans+= 1
        graph[0][y] = graph[1][y] = graph[2][y] = graph[3][y] = 0

def check_green():
    from copy import deepcopy
    global graph
    flag = 0
    for _ in range (any(graph[4]) + any(graph[5])):
        # shift
        new_graph = deepcopy(graph)
        for r in range(8, 3, -1):
            for c in range(0,4):
                new_graph[r+1][c] = graph[r][c]
        new_graph[4][0],new_graph[4][1],new_graph[4][2],new_graph[4][3] = 0,0,0,0
        flag = 1
    if flag:
        graph = deepcopy(new_graph)

def check_blue():
    from copy import deepcopy
    global graph
    flag = 0
    for _ in range(any([graph[0][4], graph[1][4], graph[2][4], graph[3][4]]) + any([graph[0][5], graph[1][5], graph[2][5], graph[3][5]])):
        new_graph = deepcopy(graph)
        for c in range(8, 3, -1):
            for r in range(0,4):
                new_graph[r][c+1] = graph[r][c]
        new_graph[0][4], new_graph[1][4], new_graph[2][4], new_graph[3][4] = 0, 0, 0, 0
        flag = 1
    if flag:
        graph = deepcopy(new_graph)
    
def move(ls):
    # for row in graph:
    #     print(row)    
    t, cx, cy = ls[-1]
    
    if t==2: #horz block
        # move horz
        # cx, cy = ls[-1]
        nx, ny = cx, cy+1
        while can_move(nx,ny):
            ny = ny+1
        ny -= 1
        # print(nx, ny)
        if cy != ny:
            # del old
            graph[cx][cy] = 0
            graph[cx][cy-1] = 0
            # new
            graph[nx][ny] = 1
            graph[nx][ny-1] = 1
            # check and pop full columns
            pop_col(nx,ny)
            pop_col(nx,ny-1)
            check_blue()
        
        # move vert
        cx, cy1, cy2 = ls[0][1], ls[0][2], ls[1][2]
        nx, ny1, ny2 = cx+1, cy1, cy2
        while can_move(nx, ny1) and can_move(nx, ny2):
            nx = nx+1
        nx -= 1
        if cx != nx:
            graph[cx][cy1], graph[cx][cy2] = 0, 0
            graph[nx][ny1], graph[nx][ny2] = 1, 1
            pop_row(nx,ny)
            check_green()
    
    elif t ==3: # vert block
        # move horz
        cy, cx1, cx2 = ls[0][2], ls[0][1], ls[1][1]
        ny, nx1, nx2 = cy+1, cx1, cx2
        while can_move(nx1, ny) and can_move(nx2, ny):
            ny = ny+1
        ny -= 1
        if cy != ny:
            graph[cx1][cy], graph[cx2][cy] = 0, 0
            graph[nx1][ny], graph[nx2][ny] = 1, 1       
            pop_col(nx1,ny)
            check_blue()
            
        # move vert
        # cx, cy = ls[-1]
        nx, ny = cx+1, cy
        while can_move(nx,ny):
            nx = nx+1
        nx -= 1
        if cx != nx:
            graph[cx][cy] = 0
            graph[cx-1][cy] = 0
            graph[nx][ny] = 1
            graph[nx-1][ny] = 1
            pop_row(nx,ny)
            pop_row(nx-1,ny)
            check_green()
            
    elif t == 1:
        # single block
        # cx, cy = ls[-1]
        # vert
        nx = cx+1
        while can_move(nx,cy):
            nx = nx+1
        nx -= 1
        if cx != nx:
            graph[cx][cy] = 0
            graph[nx][cy] = 1
            check_green()
        # horz
        ny = cy+1
        while can_move(cx,ny):
            ny = ny+1
        ny -= 1
        if cy != ny:
            graph[cx][cy] = 0
            graph[cx][ny] = 1
            check_blue()
    # for row in graph:
    #     print(row)
    # print("================")

for _ in range(N):
    t, x, y = map(int, input().split())
    if t == 1:
        graph[x][y] =1
        move([(t, x,y)])
    elif t == 2:
        graph[x][y] = graph[x][y+1] = 1
        move([(t,x,y), (t,x,y+1)])
    elif t == 3:
        graph[x][y] = graph[x+1][y] = 1
        move([(t,x,y), (t,x+1,y)])

print(ans)
cnt = 0
for r in range(0,10):
    for c in range(0,10):
        if r <=3 and c <=3 :
            continue
        elif r >=4 and c >= 4:
            continue
        if graph[r][c] == 1:
            cnt +=1
print(cnt)
    