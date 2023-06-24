
N = int(input())
nums = list(map(int, input().split()))
ops = {0:0, 1:0, 2:0, 3:0} # +, -, *, /
ns = map(int, input().split())
for i, n in enumerate(ns):
    ops[i] = n

maxi, mini = 0, 100000000
def dfs(idx, cumsum, ops):
    global maxi, mini
    if idx == N:
        maxi = max(cumsum, maxi)
        mini = min(cumsum, mini)
        return ;
    # 숫자랑 부호 더하기    
    for i, n in ops.items():
        if n == 0:
            continue
        ops[i] -= 1
        temp = cumsum
        if i == 0:
            temp += nums[idx]
        elif i == 1:
            temp -= nums[idx]
        elif i == 2:
            temp *= nums[idx]
        else:
            if temp < 0:
                temp = -1 * temp // nums[idx]
            else:
                temp //= nums[idx]
        dfs(idx+1, temp, ops)
        ops[i] += 1


dfs(1, nums[0], ops)
print(maxi)
print(mini)