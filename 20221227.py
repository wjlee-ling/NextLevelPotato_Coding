"""
solved
"""


def solution(n):
    answer = 0

    n1, n2 = 1, 2
    if n == 1:
        return n1
    if n == 2:
        return n2
    for _ in range(2, n):
        answer = (n1 + n2) % 1234567
        n1 = n2
        n2 = answer

    return answer


if __name__ == "__main__":
    ns = [4, 3]
    result = [5, 3]
    for n in ns:
        print(solution(n))

"""
1 1

2 2

3 3

4 5

5 8
1 1 1 1 1
1 1 1 2
1 1 2 1
1 2 1 1
1 2 2
2 1 1 1
2 1 2
2 2 1

6 13
1 1 1 1 1 1
1 1 1 1 2
1 1 1 2 1
1 1 2 1 1
1 2 1 1 1
2 1 1 1 1
1 1 2 2
1 2 1 2
1 2 2 1
2 1 2 1
2 1 1 2
2 2 1 1
2 2 2
"""
