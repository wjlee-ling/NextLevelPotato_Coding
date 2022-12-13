"""
solved
"""


def solution(board):
    answer = 0

    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i - 1][j - 1], board[i - 1][j], board[i][j - 1]) + 1

    for b in board:
        answer = max(answer, max(b))

    return answer**2


if __name__ == "__main__":
    board = [
        [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]],
        [[0, 0, 1, 1], [1, 1, 1, 1]],
    ]
    answer = [9, 4]

    for b in board:
        print(solution(b))
