"""
14499. 주사위 굴리기
"""


from collections import deque


def solution():
    N, M, y, x, K = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    commands = list(map(int, input().split()))

    # 동서북남
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    dice_up_down = deque([0, 0, 0, 0])  # rotate(1) => 북, rotate(-1) => 남, idx 0 : 주사위 윗면 / idx 2 : 주사위 아랫면
    dice_left_right = deque([0, 0, 0, 0])  # rotate(1) => 동, rotate(-1) => 서

    # print(dice_up_down)
    # print(dice_left_right)

    def is_valid(y, x):
        if 0 <= y < N and 0 <= x < M:
            return True
        return False

    for d in commands:
        d -= 1
        ny = y + dy[d]
        nx = x + dx[d]

        if is_valid(ny, nx):
            if d == 0:  # 동
                dice_left_right.rotate(1)
                dice_up_down[0] = dice_left_right[0]
                dice_up_down[2] = dice_left_right[2]
            if d == 1:  # 서
                dice_left_right.rotate(-1)
                dice_up_down[0] = dice_left_right[0]
                dice_up_down[2] = dice_left_right[2]
            if d == 2:  # 북
                dice_up_down.rotate(1)
                dice_left_right[0] = dice_up_down[0]
                dice_left_right[2] = dice_up_down[2]
            if d == 3:  # 남
                dice_up_down.rotate(-1)
                dice_left_right[0] = dice_up_down[0]
                dice_left_right[2] = dice_up_down[2]

            if board[ny][nx] == 0:
                board[ny][nx] = dice_up_down[2]
            elif board[ny][nx] != 0:
                dice_up_down[2] = board[ny][nx]
                dice_left_right[2] = board[ny][nx]
                board[ny][nx] = 0

            print(dice_up_down[0])
            y = ny
            x = nx


if __name__ == "__main__":
    solution()
