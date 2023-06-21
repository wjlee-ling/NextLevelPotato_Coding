"""
14503. 로봇 청소기
"""

from collections import deque


def solution():
    N, M = map(int, input().split())
    r, c, i = map(int, input().split())  # 로봇청소기 위치 (r,c), 방향 d

    board = [list(map(int, input().split())) for _ in range(N)]

    # for b in board:
    #     print(b)
    # print()

    # 북 동 남 서
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    answer = 2
    q = deque()
    q.append([r, c, i])

    def is_valid(y, x):
        if 0 <= y < N and 0 <= x < M:
            return True
        return False

    while q:
        y, x, d = q.popleft()
        board[y][x] = answer
        # print("#", y, x, d)

        flag = True
        for i in range(1, 5):
            nd = (d - 1 * i) % 4
            ny = y + dy[nd]
            nx = x + dx[nd]

            if is_valid(ny, nx) and board[ny][nx] == 0:
                flag = False
                q.append([ny, nx, nd])
                answer += 1
                break

        if flag:
            ny = y - dy[d]
            nx = x - dx[d]

            if is_valid(ny, nx) and board[ny][nx] != 1:
                q.append([ny, nx, d])
            else:
                break

        # for b in board:
        #     print(b)
        # print()

    return answer - 1


if __name__ == "__main__":
    print(solution())

"""
로봇 청소기는 다음과 같이 작동한다.

1. 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소한다.
2. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 없는 경우,
    2-1. 바라보는 방향을 유지한 채로 한 칸 후진할 수 있다면 한 칸 후진하고 1번으로 돌아간다.
    2-2. 바라보는 방향의 뒤쪽 칸이 벽이라 후진할 수 없다면 작동을 멈춘다.
3. 현재 칸의 주변 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    3-1. 반시계 방향으로 90도 회전한다.
    3-2. 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 빈 칸인 경우 한 칸 전진한다.
    3-3. 1번으로 돌아간다.
"""
