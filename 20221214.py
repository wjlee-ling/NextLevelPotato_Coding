# # Dynamic Programming
# ## 입력 크기가 작은 부분 문제 해결 후, 해당 부분의 해를 이용해서 보다 큰 문제를 해결하는 방법

# # 작은 정사각형부터 확인하고, 점점 큰 정사각형을 확인

def solution(board):
    """
    Args:
        board : 2차원 배열로 주어진 표
        
    Returns:
        표에서 1로 이루어진 가장 큰 정사각형의 넓이
    """
    r, c = len(board), len(board[0])
    
    # DP 초기 상태 설정
    dp = [[0]*c for _ in range(r)]
    dp[0] = board[0]
    for i in range(r):
        dp[i][0] = board[i][0]
    
    # DP 점화식
    for i in range(1, r):
        for j in range(1, c):
            if board[i][j] == 1:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
    
    answer = 0
    for i in range(r):
        answer = max(answer, max(dp[i]))
    
    return answer**2