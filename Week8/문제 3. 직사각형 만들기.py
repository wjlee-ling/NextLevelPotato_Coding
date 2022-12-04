# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
solved
"""

from collections import defaultdict


def solution():
    answer = 0
    N = int(input())
    sticks = list(map(int, input().split()))
    sticks_dict = defaultdict(int)
    for stick in sticks:
        sticks_dict[stick] += 1
    sticks = sorted(map(list, sticks_dict.items()), key=lambda x: -x[0])

    x = y = 0
    for stick in sticks:
        while stick[1] >= 2:
            if x == 0:
                x = stick[0]
                stick[1] -= 2
            elif y == 0:
                y = stick[0]
                stick[1] -= 2
            if x != 0 and y != 0:
                print(x, y)
                answer += x * y
                x = y = 0

    return answer


if __name__ == "__main__":
    print(solution())

"""
10 10 5 5 3 3 2 2
5 5 2 2 1 1 1 1
6 6 4 4 3 3 3 3
"""
