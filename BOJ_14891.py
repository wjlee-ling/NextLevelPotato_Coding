from collections import deque


def solution():
    gears = [deque(map(int, input())) for _ in range(4)]

    # for g in gears:
    #     print(g)
    # print()

    K = int(input())
    for _ in range(K):
        num, direction = map(int, input().split())
        num -= 1

        def check_right(start, d):
            if start > 3 or gears[start - 1][2] == gears[start][6]:
                return

            check_right(start + 1, -d)
            gears[start].rotate(d)

        def check_left(start, d):
            if start < 0 or gears[start][2] == gears[start + 1][6]:
                return

            check_left(start - 1, -d)
            gears[start].rotate(d)

        check_right(num + 1, -direction)
        check_left(num - 1, -direction)
        gears[num].rotate(direction)

        # for g in gears:
        #     print(g)
        # print()

    answer = 0
    for i in range(4):
        if gears[i][0]:
            answer += 2**i

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
