# 거리 d를 넘으면 안된다.
# d를 반지름으로 하는 원 안에 들어와있어야 한다.
# x^2 + y^2 = d^2
# x값에 따른 y값을 구하면 될 듯

import math

def solution(k, d):
    """
    Args:
        k (int) : 양의 정수
        d (int) : 원점과의 거리를 나타내는 정수
    
    Returns:
        찍히는 점의 총 개수   
    """
    answer = 0
    for x in range(0, d+1, k):
        y = int(math.sqrt(d*d - x*x))
        answer += (y // k) + 1 # x축
    
    return answer