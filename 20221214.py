'''
1로 이루어진 가장 큰 정사각형의 넓이를 찾자
DP !! 문제임을 깨닫지 못했음
'''

def solution(board):
    answer = 0
    row = len(board)
    col = len(board[0])
    # board[1][1] ~ board[row-1][col-1]
    for i in range(1, row):
        for j in range(1, col):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j-1], board[i][j-1], board[i-1][j]) + 1   
                #answer = max(answer, board[i][j]) 1*1 보드로 주어질 때

    for i in range(row):
        tmp = max(board[i])
        answer = max(answer, tmp)
        
    return answer**2