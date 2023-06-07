import math


def solution():
    answer = 0
    N = int(input())
    A = list(map(int, input().split()))
    B, C = map(int, input().split())

    answer += N
    for a in A:
        if (a - B) > 0:
            answer += math.ceil((a - B) / C)

    return answer


if __name__ == "__main__":
    print(solution())
