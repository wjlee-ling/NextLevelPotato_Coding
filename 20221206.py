import re

"""
strip()을 해줘야 하는지?
"""


def solution(s):
    # try 3 => all 통과: split(' '), 즉 스페이스 하나로만 자르도록 명시
    answer = s
    ls = []
    for token in answer.split(" "):
        ls.append(token.capitalize())
    answer = " ".join(ls)

    # try 2: re로 공백 상관없이
    # answer = s
    # while m:= re.search(r'\b[a-z][a-zA-Z0-9]*', answer):
    #     m = m.group()
    #     answer = re.sub(m, m.capitalize(), answer)

    # try 1
    # answer = s.strip()
    # ls = []
    # for token in answer.split():
    #     ls.append(token.capitalize())
    # answer = ' '.join(ls)

    return answer
