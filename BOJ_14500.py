"""
테트로미노
"""


def solution():
    # fmt:off
    tetrominos = [[[1, 1, 1, 1]], 
                  
                  [[1], 
                   [1], 
                   [1], 
                   [1]],
                  
                  [[1, 1], 
                   [1, 1]], 
                  
                  [[1, 0], 
                   [1, 0], 
                   [1, 1]], 
                  
                  [[1, 0], 
                   [1, 1], 
                   [0, 1]], 
                  
                  [[1, 1, 1], 
                   [0, 1, 0]]]
    # fmt:on

    def rot(shape, n):
        temp = shape[:]
        for i in range(n):
            temp = list(reversed(list(map(list, zip(*temp)))))
        return temp

    def symmetry(shape):
        return list(map(list, zip(*shape)))

    for i in range(3, 6):
        temp = tetrominos[i]
        tetrominos.append(symmetry(temp))
        for n in range(1, 4):
            temp = rot(temp, n)
            if temp not in tetrominos:
                tetrominos.append(temp)
            if symmetry(temp) not in tetrominos:
                tetrominos.append(symmetry(temp))

    # for t in tetrominos:
    #     print(t)
    # print()

    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 0

    for r in range(N):
        for c in range(M):
            for t in tetrominos:
                result = 0
                for i in range(len(t)):
                    for j in range(len(t[0])):
                        if 0 <= r + i < N and 0 <= c + j < M and t[i][j] == 1:
                            result += board[r + i][c + j]
                answer = max(answer, result)

    print(answer)


if __name__ == "__main__":
    solution()
