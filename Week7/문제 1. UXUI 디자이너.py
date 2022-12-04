# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

"""
4 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 3
: 3

4 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 3
: 1 2 3 4
"""

from collections import defaultdict

N, M = map(int, input().split())

users = defaultdict(int)
for _ in range(M):
    _, *events = list(map(int, input().split()))
    for event in events:
        users[event] += 1
# print(users)

max_ = max(users.values())
# print(max_)
answers = []
for key, value in users.items():
    # print(key, value)
    if value == max_:
        answers.append(key)

for answer in sorted(answers, reverse=True):
    print(answer, end=" ")
