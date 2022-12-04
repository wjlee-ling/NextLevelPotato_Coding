# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    answer = 1
    n = int(input())
    bridges = list(map(int, input().split()))

    for bridge in bridges:
        answer *= bridge
    return answer


if __name__ == "__main__":
    print(solution())
