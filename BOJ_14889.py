from itertools import combinations

N = int(input())
indices = [0] * N # 0: 스타트팀 1: 링크팀
# total_sum = 0
ans = 101 * N * N
scores = []
for _ in range(N):
    row = list(map(int, input().split()))
    # total_sum += sum(row)
    scores.append(row)

def get_sum(ls, value=0):
    ls = [k for k, v in enumerate(ls) if v == value]
    c = combinations(ls, 2)
    ret = 0
    for (x,y) in c:
        ret += scores[x][y] + scores[y][x]
    return ret

def step(idx, cnt):
    global ans
    if cnt == N//2:
        rest = get_sum(indices) # a팀
        cumsum = get_sum(indices, 1) # B 팀
        ans = min(ans, abs(rest-cumsum))
        return ;
    
    if N-1-idx >= N//2-cnt and idx <= N-1:
        # 이번 idx는 링크팀
        new_power = 0 
        indices[idx] = 1
        step(idx+1, cnt+1)
        
        # backtracking
        indices[idx] = 0
        step(idx+1, cnt)
step(0, 0)
print(ans)