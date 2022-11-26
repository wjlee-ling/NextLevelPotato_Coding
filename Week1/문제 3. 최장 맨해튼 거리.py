# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    answer = 0
    distances = list(map(int, input().split()))
    distances.sort()

    answer = abs(distances[0] - distances[-1]) + abs(distances[1] - distances[-2])

    return answer


if __name__ == "__main__":
    print(solution())

"""
1 3 5 10
-10 -3 -1 5
"""
