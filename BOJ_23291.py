"""
23291. 어항정리
"""


from collections import deque
from copy import deepcopy


def solution():
    N, K = map(int, input().split())
    board = []
    board.append(deque(list(map(int, input().split()))))
    # print(board)

    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]

    # 물고기가 가장 적은 어항에 물고기 한 마리 넣기
    def push_fish(board):
        min_num_fish = min(board[0])
        for i in range(len(board[0])):
            if board[0][i] == min_num_fish:
                board[0][i] += 1

        return board

    # 가장 왼쪽 어항을 위에 쌓기
    def stack_bowls(board):
        num_fish = board[0].popleft()
        board.append(deque([num_fish]))

        return board

    # 어항 90도 회전
    def rotate_90_clockwise(board):
        temp_board = [[0] * len(board) for _ in range(len(board[0]))]
        for i in range(len(board[0])):
            for j in range(len(board)):
                temp_board[i][j] = board[j][len(board[0]) - 1 - i]

        return temp_board

    # 2개 이상 쌓인 어항들을 분리하고 공중부양
    def fly_bowls(board):
        while True:
            if len(board) > len(board[0]) - len(board[-1]):
                break

            will_fly_bowls = []
            will_fly_bowls_row = len(board)
            will_fly_bowls_col = len(board[-1])

            for i in range(will_fly_bowls_row):
                q = deque()
                for _ in range(will_fly_bowls_col):
                    q.append(board[i].popleft())
                will_fly_bowls.append(q)

            board = [board[0]]
            rotated_bowls = rotate_90_clockwise(will_fly_bowls)
            for row in rotated_bowls:
                board.append(deque(row))

            # print(f"fly bowls {board}")

        return board

    # 공중부양 후 어항의 물고기 수 조절
    def fix_fish_num(board):
        temp_board = [[0] * len(board[x]) for x in range(len(board))]
        for y in range(len(board)):
            for x in range(len(board[y])):
                for d in range(4):
                    ny = y + dy[d]
                    nx = x + dx[d]

                    if 0 <= ny < len(board) and 0 <= nx < len(board[ny]):
                        # 현재 칸이 인접 칸보다 크다면
                        if board[y][x] > board[ny][nx]:
                            d = (board[y][x] - board[ny][nx]) // 5
                            if d >= 1:
                                temp_board[y][x] -= d
                        # 현재 칸이 인접 칸보다 작다면
                        else:
                            d = (board[ny][nx] - board[y][x]) // 5
                            if d >= 1:
                                temp_board[y][x] += d

        for i in range(len(board)):
            for j in range(len(board[i])):
                board[i][j] += temp_board[i][j]

        return board

    # 다시 어항을 일렬로 놓음
    def put_bowl_in_a_row(board):
        q = deque()

        for c in range(len(board[-1])):
            for r in range(len(board)):
                q.append(board[r][c])

        for c in range(len(board[-1]), len(board[0])):
            q.append(board[0][c])

        result = list()
        result.append(q)

        return result

    # 180 도 회전
    def rotate_180_clockwise(board):
        temp_board = []

        for i in reversed(range(len(board))):
            board[i].reverse()
            temp_board.append(board[i])

        return temp_board

    # 절반씩 공중부양 2번
    def fly_bowls2(board):
        left1 = []
        left2 = []
        temp_board1 = deque()
        for i in range(N // 2):
            temp_board1.append(board[0].popleft())
        left1.append(temp_board1)
        rotated_left1 = rotate_180_clockwise(left1)
        board += rotated_left1

        for i in range(2):
            temp_board2 = deque()
            for j in range(N // 4):
                temp_board2.append(board[i].popleft())
            left2.append(temp_board2)
        rotated_left2 = rotate_180_clockwise(left2)
        board += rotated_left2

        # print(f"fly bowls2 {board}")

        return board

    # 물고기가 가장 많은 어항과 가장 적은 어항의 차이를 구하는 함수
    def get_result(board):
        temp = board[0]
        result = max(temp) - min(temp)

        return result

    answer = 0
    while True:
        result = get_result(board)
        if result <= K:
            break

        board = push_fish(board)
        # print(f"push fish {board}")

        board = stack_bowls(board)
        # print(f"stack bowls {board}")

        board = fly_bowls(board)

        board = fix_fish_num(board)
        # print(f"fix fish num {board}")

        board = put_bowl_in_a_row(board)
        # print(f"put bowl in a row {board}")

        board = fly_bowls2(board)

        board = fix_fish_num(board)
        # print(f"fix fish num {board}")

        board = put_bowl_in_a_row(board)
        # print(f"put bowl in a row {board}")
        # print()
        answer += 1

    return answer


if __name__ == "__main__":
    print(solution())
