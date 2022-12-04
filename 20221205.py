"""
solved
"""


def solution(s):
    answer = ""
    s = list(map(int, s.split()))
    answer = f"{min(s)} {max(s)}"
    return answer


if __name__ == "__main__":
    s = ["1 2 3 4", "-1 -2 -3 -4", "-1 1"]
    results = ["1 4", "-4 -1", "-1 -1"]
    for inputs in s:
        print(solution(inputs))
