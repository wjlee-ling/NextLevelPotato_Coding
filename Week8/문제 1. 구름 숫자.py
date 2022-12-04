# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
"""
solved
"""


def solution():
    answer = ""
    N = int(input())
    seq = input()

    cloud_nums = {1: "qw", 2: "as", 3: "zx", 4: "we", 5: "sd", 6: "xc", 7: "er", 8: "df", 9: "cv", 0: "ze"}
    cloud_words = {v: k for k, v in cloud_nums.items()}
    for i in range(N - 1):
        cw = seq[i : i + 2]
        if cw in cloud_words.keys():
            answer += str(cloud_words[cw])

    return answer


if __name__ == "__main__":
    print(solution())
