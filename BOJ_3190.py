"""
3190. 뱀
"""

from collections import deque


def solution():
    N = int(input())
    board = [[0] * N for _ in range(N)]
    K = int(input())
    for _ in range(K):
        y, x = map(int, input().split())
        board[y - 1][x - 1] = 1

    # 우하좌상
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]

    L = int(input())
    directions = {}
    for _ in range(L):
        X, C = input().split()
        directions[int(X)] = C

    snake = deque()
    snake.append([0, 0])  # 뱀 전체 위치
    snake_head = [0, 0]  # 뱀 머리 위치
    d = 0  # 진행 방향
    t = 0
    while True:
        y, x = snake_head
        if t in directions:
            if directions[t] == "L":
                d = (d - 1) % 4
            elif directions[t] == "D":
                d = (d + 1) % 4

        ny = y + dy[d]
        nx = x + dx[d]

        if not (0 <= ny < N and 0 <= nx < N):  # 보드를 벗어나면 종료
            return t + 1
        if [ny, nx] in snake:  # 몸과 부딪히면 종료
            return t + 1

        if board[ny][nx] == 0:
            snake.popleft()
        elif board[ny][nx] == 1:  # 사과를 먹었으면 삭제
            board[ny][nx] = 0
        snake.append([ny, nx])
        snake_head = [ny, nx]
        # print(snake)

        t += 1


if __name__ == "__main__":
    print(solution())
