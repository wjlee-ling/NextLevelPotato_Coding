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
    for i in [0,1]:
        # print(f"dir == {i} step == {step}")
        push_map(i)
        print(step )
        for row in graph:
            print(row)
        print("================")
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

    for idx in range(len(arr)-1):
        # 중간의 빈칸 없애기
        cnt = 0
        while arr[idx] == 0:
            arr.append(arr.pop(idx))
            cnt += 1
            if cnt >= N-idx:
                break

        if arr[idx] == arr[idx+1]:
            arr[idx] = arr[idx]*2
            ans = max(arr[idx], ans) ## 최댓값으로 업뎃
            arr.pop(idx+1)
            arr.append(0)
    return arr

def early_stop(step):
    global ans
    maxi = 0
    for i in range(N):
        for j in range(N):
            maxi = max(maxi, graph[i][j])
    
    if maxi * 2 **(5-step) < ans:
        return True
    return False

dfs()
ans = max(ans, given_max)
print(ans)