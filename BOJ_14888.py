N = int(input())
nums = list(map(int, input().split()))
ops = {0:0, 1:0, 2:0, 3:0} # +, -, *, /
ns = map(int, input().split())
for i, n in enumerate(ns):
    ops[i] = n

maxi, mini = -float("inf"), float("inf") ## 💥💥 처음에 maxi == 0 으로 init 해서 틀렸음 => 최종 max값이 음수일 수도 있음!!
def dfs(idx, cumsum):
    # [1, 2, 3] => dfs 호출할 때마다 부호랑 숫자 처리
    global maxi, mini, ops
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
            temp = int(temp/nums[idx])
        dfs(idx+1, temp)
        ops[i] += 1


dfs(1, nums[0])
print(maxi)
print(mini)