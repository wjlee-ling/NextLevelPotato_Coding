import sys
from collections import deque

# https://jie0025.tistory.com/209 수정본
# 테스트케이스는 다 통과하는데 시간 초과!!! ->  num_zero, num_new_two 추가

n, m = map(int, sys.stdin.readline().split())
graph = []
cont = [] # contaminated area
ans = 0
num_zeros = 0

# build graph and get ls of 2s
for i in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))
    for j in range(m):
        if graph[i][j] == 2:
            cont.append((i,j))
        elif graph[i][j] == 0:
            num_zeros += 1

def build_wall(count, num_zeros):
    if count == 3:
        # count 2s
        bfs(num_zeros)
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1 # wall
                build_wall(count+1, num_zeros)
                graph[i][j] = 0

def bfs(num_zeros):
    # contaminate 0s 
    q = deque(cont)  # origins of 2s
    seen = set()
    moves = [(0,1), (1,0), (0,-1), (-1,0)]
    num_new_two = 0
    while q:
        x,y = q.popleft()
        
        for dx,dy in moves:
            nx = dx+x
            ny = dy+y

            if (0<=nx<n) and (0<=ny<m) and (nx,ny) not in seen:
                if graph[nx][ny] == 0:
                    # contaminate 0 with 2
                    seen.add((nx,ny)) # prevent re-contamination
                    num_new_two += 1
                    q.append((nx,ny))

    global ans
    ans = max(ans, num_zeros-3-num_new_two)

build_wall(0, num_zeros)
print(ans)

# try 1:
# '2' 주변을 막기
# n, m = map(int, input().split())

# def envr(i,j):
#     # get environment of '2'
#     moves = [(0,1), (1,0), (-1,0), (0,-1)]
#     ls = []
#     for dx, dy in moves:
#         nx, ny = i+dx, j+dy
#         if nx < 0 or ny < 0 or nx >= n or ny >= m:
#             continue
#         # !! 2 2 ????????
#         if graph[nx][ny] == 0:
#             ls.append((nx,ny))
#     return ls
        
# # find empty cells around 2 and fill in
# targets = []
# graph = []
# for i in range(n):
#     row = list(map(int, input().split()))
#     graph.append(row)

# for i in range(n):
#     # need full graph 
#     for j in range(m):
#         if row[i][j] == 2:
#             targets.append(envr(i,j))
