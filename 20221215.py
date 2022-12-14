# 어피치와 라이언이 특정 점수에 맞힌 화살 개수가 같은 경우 어피치가 득점

# 화살의 개수 n이 크지는 않으므로 완전탐색으로 풀 수 있음 (n <= 10)
# DFS를 이용

from copy import deepcopy
max_diff, answer = 0, []

def dfs(a_score, l_score, cnt, idx, board, info, n):
    """
    Args:
        a_score (int): 어피치 점수
        l_score (int): 라이언 점수
        cnt (int): 화살을 쏜 개수 
        idx (int): 과녁판 점수 인덱스 
        board (_type_): 어피치가 맞힌 과녁의 점수 개수(10점부터 0점까지)를 순서대로 담은 정수 배열
        info (list) : 어피치가 맞힌 과녁의 점수 개수(10점부터 0점까지)를 순서대로 담은 정수 배열
        n (int): 화살의 개수
    """
    global max_diff, answer

    # 더 이상 쏠 화살이 없는 경우
    if cnt > n:
        return
    
    # 0점 과녁 idx까지 온 경우 점수 계산 및 업데이트
    if idx == 11:
        diff = l_score - a_score
        if diff == max_diff:
            for i, j in zip(board[::-1], answer[::-1]):
                # 가장 낮은 점수를 더 많이 맞힌 경우를 return 해주기 위해 확인
                if i > j:
                    board[-1] = n - cnt
                    answer = board
                    break
                elif i < j: 
                    break
        
        elif diff > max_diff:
            board[-1] = n - cnt
            answer = board
            max_diff = diff
        return

    # 현재 idx의 어피치 과녁 화살 개수
    a_cnt = info[idx]

    # 라이언의 경우의 수 2가지
    ## 1. 어피치보다 한 발 더 맞추기
    ## 2. 해당 점수 포기
    for i in [a_cnt+1, 0]:
        board2 = deepcopy(board)
        # 1. 어피치보다 한 발 더 맞추기
        if i == a_cnt+1:
            board2[idx] = a_cnt+1
            dfs(a_score, l_score+(10-idx), cnt+a_cnt+1, idx+1, board2, info, n)
        # 2. 해당 점수 포기
        else:
            # 2.1 어피치는 화살을 맞춘 경우
            if info[idx] > 0:
                dfs(a_score+(10-idx), l_score, cnt, idx+1, board2, info, n)
            # 2.2 어피치도 못맞춘 경우
            else:
                dfs(a_score, l_score, cnt, idx+1, board2, info, n)

def solution(n, info):
    """
    Args:
        n (int) : 화살의 개수
        info (list) : 어피치가 맞힌 과녁의 점수 개수(10점부터 0점까지)를 순서대로 담은 정수 배열
    
    Returns:
        라이언이 어피치를 가장 큰 점수차이로 우승하기 위해 맞혀야하는 10점부터 0점까지의 화살 개수 정수 배열
        라이언이 우승할 수 없는 경우 [-1]
    """
    global max_diff, answer

    board = [0]*11 

    dfs(0, 0, 0, 0, board, info, n)

    return answer or [-1]