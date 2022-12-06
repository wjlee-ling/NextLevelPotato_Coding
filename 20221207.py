"""
solved
"""


def solution(n, times):
    answer = 0

    start, end = 1, max(times) * n

    while start <= end:
        mid = (start + end) // 2
        people = 0
        for time in times:
            people += mid // time
            if people >= n:
                break

        if people >= n:
            answer = mid
            end = mid - 1
        elif people < n:
            start = mid + 1

    return answer


if __name__ == "__main__":
    nums = [6]
    times = [[7, 10]]
    results = [28]
    for n, t in zip(nums, times):
        print(solution(n, t))
