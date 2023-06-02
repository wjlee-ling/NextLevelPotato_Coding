from copy import deepcopy

xmoves = [-1,0,0,1] # 상우하좌
ymoves = [0,1,0,-1] 
ans = 2
given_max = 2
graph = []

N = int(input())
for _ in range(N):
    row = list(map(int, input().split()))
    given_max = max(max(row), given_max)
    graph.append(row)

def dfs(step=1):
    global ans, graph
    
    if step == 6:
        return

    original_graph = deepcopy(graph)
    for i in range(4):
        push_map(i)
        dfs(step+1)
        graph = deepcopy(original_graph)

def push_map(dir):
    """주어진 방향으로 밀기"""
    global ans
    if dir in [0,2]:
        # 상 또는 하
        temp_graph = list(map(list, zip(*graph))) # 세로로 뽑아내기
        for (i, col) in enumerate(temp_graph):
            if dir == 2 :
                # 아래서부터 작업
                temp_graph[i] = push_array(col[::-1])[::-1]
            else:
                temp_graph[i] = push_array(col)

        for i in range(N):
            for j in range(N):
                graph[j][i] = temp_graph[i][j]
    else:
        # 우 또는 좌
        for i, row in enumerate(graph):
            if dir == 1:
                # 우
                graph[i] = push_array(row[::-1])[::-1]
            else:
                graph[i] = push_array(row) 


def push_array(arr):
    global ans
    if sum(arr) == 0:
        return arr
    
    # 중간에 있는 0 지우기
    cnt = 0
    while 0 in arr:
        arr.remove(0)
        cnt += 1
    arr.extend([0]*cnt)

    for idx in range(N-1):
        if arr[idx] == arr[idx+1]:
            arr[idx] = arr[idx]*2
            ans = max(arr[idx], ans) ## 최댓값으로 업뎃
            arr.pop(idx+1)
            arr.append(0)
    return arr


dfs()
ans = max(ans, given_max)
print(ans)


# #case 1
# 5
# 2 2 4 8 16
# 0 0 0 0 0
# 0 0 0 0 0
# 0 0 0 0 0
# 2 2 4 8 16 