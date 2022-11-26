# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def solution():
    answer = []
    N = int(input())
    peaks = list(map(int, input().split()))

    for i in range(N):
        max_peak = 0
        count = 0
        for j in range(i - 1, -1, -1):
            if peaks[j] > max_peak:
                count += 1
            max_peak = max(peaks[j], max_peak)
        answer.append(count)

    return answer


if __name__ == "__main__":
    print(*solution())


"""
시간초과
"""
