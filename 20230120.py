"""
프로그래머스
개인정보 수집 유효기간
https://school.programmers.co.kr/learn/courses/30/lessons/150370

solved
"""


def solution(today, terms, privacies):
    answer = []
    today_num = str_to_int(today)
    print(today_num)

    term_dict = dict()
    for term in terms:
        type_, time = term.split()
        term_dict[type_] = int(time)
    print(term_dict)

    for i, privacy in enumerate(privacies):
        start, type_ = privacy.split()
        start_num = str_to_int(start)
        time = term_dict[type_]

        print(today_num, start_num + time * 28)
        if today_num >= start_num + time * 28:
            answer.append(i + 1)

    return answer


def str_to_int(date):
    y, m, d = map(int, date.split("."))
    return y * 12 * 28 + m * 28 + d


if __name__ == "__main__":
    today = [
        "2022.05.19",
        "2020.01.01",
    ]
    terms = [
        ["A 6", "B 12", "C 3"],
        ["Z 3", "D 5"],
    ]
    privacies = [
        ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"],
        ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"],
    ]
    result = [[1, 3], [1, 4, 5]]

    for td, term, privacy in zip(today, terms, privacies):
        print(solution(td, term, privacy))
