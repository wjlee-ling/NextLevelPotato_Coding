"""
14891. 톱니바퀴
"""

from collections import deque


def solution():
    gears = [deque(map(int, input())) for _ in range(4)]

    # for g in gears:
    #     print(g)
    # print()

    def is_valid(idx):
        if 0 <= idx < len(gears):
            return True
        return False

    def left(idx, direction):
        if not is_valid(idx) or gears[idx + 1][6] == gears[idx][2]:
            return

        left(idx - 1, -direction)
        gears[idx].rotate(direction)

    def right(idx, direction):
        if not is_valid(idx) or gears[idx - 1][2] == gears[idx][6]:
            return

        right(idx + 1, -direction)
        gears[idx].rotate(direction)

    answer = 0
    K = int(input())
    for _ in range(K):
        num, direction = map(int, input().split())
        num -= 1

        left(num - 1, -direction)
        right(num + 1, -direction)
        gears[num].rotate(direction)
        # for g in gears:
        #     print(g)
        # print()

    for i in range(len(gears)):
        answer += gears[i][0] * 2**i

    print(answer)


if __name__ == "__main__":
    solution()

"""
1번 톱니바퀴의 idx2와 2번 톱니바퀴의 idx6
2번 톱니바퀴의 idx2와 3번 톱니바퀴의 idx6
3번 톱니바퀴의 idx2와 4번 톱니바퀴의 idx6

1 반시계 2 시계 3 반시계 4 시계
1 시계 2 반시계 3 시계 4 반시계
"""
