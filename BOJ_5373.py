"""
큐빙
"""


from copy import deepcopy


def solution():
    n = int(input())

    # wyrogb
    origin_cubes = [
        [["w"] * 3 for _ in range(3)],
        [["y"] * 3 for _ in range(3)],
        [["r"] * 3 for _ in range(3)],
        [["o"] * 3 for _ in range(3)],
        [["g"] * 3 for _ in range(3)],
        [["b"] * 3 for _ in range(3)],
    ]

    # for c in origin_cubes:
    #     print(c)
    # print()

    def clockwise(arr):  # 시계방향으로 k번 만큼 회전
        tmp = arr[0][0]
        arr[0][0] = arr[2][0]
        arr[2][0] = arr[2][2]
        arr[2][2] = arr[0][2]
        arr[0][2] = tmp

        tmp = arr[0][1]
        arr[0][1] = arr[1][0]
        arr[1][0] = arr[2][1]
        arr[2][1] = arr[1][2]
        arr[1][2] = tmp

    def U(c):
        if c == "+":
            k = 1
        else:
            k = 3
        for _ in range(k):
            clockwise(cube[0])
            tmp = cube[2][0][0], cube[2][0][1], cube[2][0][2]
            cube[2][0][0], cube[2][0][1], cube[2][0][2] = cube[5][2][0], cube[5][1][0], cube[5][0][0]
            cube[5][2][0], cube[5][1][0], cube[5][0][0] = cube[3][2][2], cube[3][2][1], cube[3][2][0]
            cube[3][2][2], cube[3][2][1], cube[3][2][0] = cube[4][0][2], cube[4][1][2], cube[4][2][2]
            cube[4][0][2], cube[4][1][2], cube[4][2][2] = tmp

    def D(c):
        if c == "+":
            k = 1
        else:
            k = 3
        for _ in range(k):
            clockwise(cube[1])
            tmp = cube[5][0][2], cube[5][1][2], cube[5][2][2]
            cube[5][0][2], cube[5][1][2], cube[5][2][2] = cube[2][2][2], cube[2][2][1], cube[2][2][0]
            cube[2][2][2], cube[2][2][1], cube[2][2][0] = cube[4][2][0], cube[4][1][0], cube[4][0][0]
            cube[4][2][0], cube[4][1][0], cube[4][0][0] = cube[3][0][0], cube[3][0][1], cube[3][0][2]
            cube[3][0][0], cube[3][0][1], cube[3][0][2] = tmp

    def R(c):
        if c == "+":
            k = 1
        else:
            k = 3
        for _ in range(k):
            clockwise(cube[5])
            tmp = cube[0][0][2], cube[0][1][2], cube[0][2][2]
            cube[0][0][2], cube[0][1][2], cube[0][2][2] = cube[2][0][2], cube[2][1][2], cube[2][2][2]
            cube[2][0][2], cube[2][1][2], cube[2][2][2] = cube[1][0][2], cube[1][1][2], cube[1][2][2]
            cube[1][0][2], cube[1][1][2], cube[1][2][2] = cube[3][0][2], cube[3][1][2], cube[3][2][2]
            cube[3][0][2], cube[3][1][2], cube[3][2][2] = tmp

    def L(c):
        if c == "+":
            k = 1
        else:
            k = 3
        for _ in range(k):
            clockwise(cube[4])
            tmp = cube[0][0][0], cube[0][1][0], cube[0][2][0]
            cube[0][0][0], cube[0][1][0], cube[0][2][0] = cube[3][0][0], cube[3][1][0], cube[3][2][0]
            cube[3][0][0], cube[3][1][0], cube[3][2][0] = cube[1][0][0], cube[1][1][0], cube[1][2][0]
            cube[1][0][0], cube[1][1][0], cube[1][2][0] = cube[2][0][0], cube[2][1][0], cube[2][2][0]
            cube[2][0][0], cube[2][1][0], cube[2][2][0] = tmp

    def F(c):
        if c == "+":
            k = 1
        else:
            k = 3
        for _ in range(k):
            clockwise(cube[2])
            tmp = cube[0][2][0], cube[0][2][1], cube[0][2][2]
            cube[0][2][0], cube[0][2][1], cube[0][2][2] = cube[4][2][0], cube[4][2][1], cube[4][2][2]
            cube[4][2][0], cube[4][2][1], cube[4][2][2] = cube[1][0][2], cube[1][0][1], cube[1][0][0]
            cube[1][0][2], cube[1][0][1], cube[1][0][0] = cube[5][2][0], cube[5][2][1], cube[5][2][2]
            cube[5][2][0], cube[5][2][1], cube[5][2][2] = tmp

    def B(c):
        if c == "+":
            k = 1
        else:
            k = 3
        for _ in range(k):
            clockwise(cube[3])
            tmp = cube[0][0][0], cube[0][0][1], cube[0][0][2]
            cube[0][0][0], cube[0][0][1], cube[0][0][2] = cube[5][0][0], cube[5][0][1], cube[5][0][2]
            cube[5][0][0], cube[5][0][1], cube[5][0][2] = cube[1][2][2], cube[1][2][1], cube[1][2][0]
            cube[1][2][2], cube[1][2][1], cube[1][2][0] = cube[4][0][0], cube[4][0][1], cube[4][0][2]
            cube[4][0][0], cube[4][0][1], cube[4][0][2] = tmp

    for _ in range(n):
        num = int(input())
        commands = list(input().split())
        # print(commands)

        cube = deepcopy(origin_cubes)
        for command in commands:
            face, direction = command
            locals()[face](direction)

        for c in cube[0]:
            print("".join(c))

        # for c in cube:
        #     print(c)
        # print()


if __name__ == "__main__":
    solution()

"""
1(상) : white
2(하) : yellow
3(전) : red
4(후) : orange
5(좌) : green
6(우) : blue

돌렸을 때
상 : 전후좌우(3,4,5,6)
하 : 전후좌우(3,4,5,6)
전 : 상하좌우(1,2,5,6)
후 : 상하좌우(1,2,5,6)
좌 : 상하전후(1,2,3,4)
우 : 상하전후(1,2,3,4)

시계방향 / 반시계방향
상, 하 회전 : 전 -> 좌 -> 후 -> 우 -> 전 / 전 -> 우 -> 후 -> 좌 -> 전 (row 기준 회전)
1, 2          3 -> 5 -> 4 -> 6 -> 3    / 3 -> 6 -> 4 -> 5 -> 3
전, 후 회전 : 상 -> 우 -> 하 -> 좌 -> 상 / 상 -> 좌 -> 하 -> 우 -> 상 (row 기준 회전)
3, 4          1 -> 6 -> 2 -> 5 -> 1    / 1 -> 5 -> 2 -> 6 -> 1
좌, 우 회전 : 상 -> 전 -> 하 -> 후 -> 상 / 상 -> 후 -> 하 -> 전 -> 상 (column 기준 회전)
5, 6          1 -> 3 -> 2 -> 4 -> 1    / 1 -> 4 -> 2 -> 3 -> 1
"""


# def rotate(arr):  # 반시계방향 회전
#     return list(reversed(list(map(list, zip(*arr)))))


# temp = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for t in temp:
#     print(t)
# print()

# for b in rotate(temp):
#     print(b)
# print()
