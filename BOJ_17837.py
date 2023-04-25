from collections import defaultdict
N, K = map(int, input().split())
graph = []
moves = {1:(0,1), 2:(0,-1), 3:(-1,0), 4:(1,0)}
stones = [] # {ith: coord}
stacks = defaultdict(list) # {coord: stack}
heading = []

for _ in range(N):
    row  = list(map(int, input().split()))
    graph.append(row)

for i in range(K):
    x, y, h = map(int, input().split())
    stones.append((x-1,y-1))
    heading.append(h)
    stacks[(x-1,y-1)].append(i)

def run(cx, cy, i):
    h = heading[i]
    stack = []
    (dx, dy) =  moves[h]
    while stacks[(cx,cy)]:
        stack.append(stacks[(cx,cy)].pop())
        if stack[-1] == i:
            break
    nx,ny = cx+dx, cy+dy
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        # out of bounds
        res = do_blue(cx,cy,stack)

    else:
        if graph[nx][ny] == 0:
            res = do_white(nx,ny,stack)
        elif graph[nx][ny]== 1:
            res = do_red(nx,ny,stack)
        else:
            res = do_blue(cx,cy,stack)
    return res
    
def do_white(nx,ny, new_input:list):
    while new_input:
        i = new_input.pop()
        stacks[(nx,ny)].append(i)
        stones[i] = (nx,ny)
    if len(stacks[(nx,ny)]) >= 4:
        return True
    return False
        
def do_red(nx,ny, new_input:list):
    stacks[(nx,ny)] += new_input
    for new in new_input:
        stones[new] = (nx,ny)
    if len(stacks[(nx,ny)]) >= 4:
        return True
    return False
  
def do_blue(cx,cy,stack):
    for new in stack:
        heading[new] = (heading[new]+1) if heading[new]%2==1 else (heading[new]-1)
    h = heading[stack[-1]]
    (dx, dy) =  moves[h]

    nx,ny = cx+dx, cy+dy
    if nx < 0 or nx >= N or ny < 0 or ny >= N:
        # out of bounds
        res = do_white(cx,cy,stack)
    else:
        if graph[nx][ny] == 0:
            res = do_white(nx,ny,stack)
        elif graph[nx][ny]== 1:
            res = do_red(nx,ny,stack)
        else:
            res = do_white(cx,cy,stack)
    return res

step = 1
flag = False
while True:
    if step >= 1000:
        step = -1
        break
    for i in range(K):
        (cx, cy) = stones[i]
        res = run(cx, cy, i)
        if res:
            flag = True 
            break
    print(f"step: {step}  =============")
    for k, val in stacks.items():
        if len(val) > 0:
            print(k, val) 
    print(heading)
    if flag:
        break
    step+=1
print(step)
    