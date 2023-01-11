def solution(n, k, enemy):
    """
    가장 적 많을 때 무적권 사용. 
    """
    cumsum = 0
    stack = [] # in descending order
    for i, num in enumerate(enemy):
        if cumsum+num > n:
            break
        cumsum += num
        rest = []
        while stack and stack[-1] < num:
            rest.append(stack.pop())
        if rest:
            stack.append(num)
            while rest and len(stack) < k:
                stack.append(rest.pop())
    end_idx = i + k # 끝나느 인덱스, 갯수 아님
    cumsum -= sum(stack) # 무적권을 최대 라운드에서 사용한만큼 cumsum에서 빼기
    
    for i, num in enumerate(enemy[end_idx+1:]):
        if cumsum+num >= n:
            break
        cusmum += num
    
    return i
