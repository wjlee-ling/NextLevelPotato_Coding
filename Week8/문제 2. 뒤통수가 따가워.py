# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
solved
"""


def solution():
    answer = []
    height = []
    N = int(input())
    peaks = list(map(int, input().split()))

    for i in range(N):
        answer.append(len(height))
        # print("answer : ", answer)
        while height and height[-1] <= peaks[i]:
            height.pop()
        height.append(peaks[i])
        # print("now : ", peaks[i])
        # print("h :", height)

    return answer


if __name__ == "__main__":
    print(*solution())
