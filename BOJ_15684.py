from collections import defaultdict, Counter
N,M,H = map(int, input().split()) # 세로, 가로
edges = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    edges[b].append((a,b+1)) # a번 점선 높이에서 세로선 (b,b+1) 이음
    edges[b+1].append((a,b-1))

def dfs(c, r, edges):
    # 맨 마지막의 세로 선 인덱스 리턴
    # base
    if r >= M: 
        return c;
    for (h, nc) in edges[c]:
        if h == r: # same level
            return dfs(nc, r+1)    
        
def get_odd_cols(edges):
    # a와 (a+1) 사이 간선이 짝수개여야 돌아갈 수 있음
    fixes = []
    for idx in range(1, N):
        for ele in [ele for ele in edges[idx] if ele[1]]
        
        cnt_curr = len([ele for ele in edges[i] if ele[1] == i+1])
        cnt_next = len([ele for ele in edges[i+1] if ele[1] == i])
        if cnt_curr != cnt_next:
            return i
    return 0
        
def add_edge(edges, idx):
    global ans
    ans += 1
    edges[idx].append()

def search(edges):
    while len(results) != N:
        idx_fix =  get_odd_col(edges)
        if get_odd_col(edges) != 0:
            add_edge(edges, idx_fix)
        
        results = [] # 되돌아오는 열의 인덱스
        for cidx in range(1, N+1):
            result = dfs(cidx, 1, edges)
            if result == cidx:
                results.append(cidx)
            else:
                break
    