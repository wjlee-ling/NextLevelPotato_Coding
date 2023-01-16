# 도둑질
# https://school.programmers.co.kr/learn/courses/30/lessons/42897
def solution(money):
    """
    (t에서 t+2 or t+3)까지 갈 수 있다.
    1st fail -> 원형 고려 안함.
    """
    from collections import defaultdict
    answer = 0
    money.extend([money[0], money[1]])
    cumsum = defaultdict(int)
    _len = len(money)
    for idx, m in enumerate(money):
        if idx in [0,1]:
            cumsum[idx] = m
        curr = cumsum[idx] # cumsum fo current node
        if idx+2 <= _len-1: 
        # if step == 2
            cumsum[idx+2] = max(cumsum[idx+2], curr+money[idx+2])
        if idx+3 <= _len-1:
        # if step == 3
            cumsum[idx+3] = curr+money[idx+3]
    answer = max(cumsum[_len-3], cumsum[_len-4])
    return answer
