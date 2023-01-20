# 모든 달은 28일까지

# today를 year, month, day로 나누기
# privacies를 돌면서 개인정보수집날짜가 today보다 이전이면 answer에 추가

# 유효기간 12개월, 2021년 1월 5일에 수집되었다면 2022년 1월 4일까지만 보관 가능, 2022년 1월 5일부터 파기해야함

from collections import defaultdict

def solution(today, terms, privacies):
    """_summary_

    Args:
        today (str):  "YYYY.MM.DD"
        terms (List[str]): ["약관종류 유효기간", ...]
        privacies (List[str]): ["개인정보수집날짜 약관종류", ...]

    Returns:
        List : 파기해야 할 개인정보의 번호를 오름차순으로 정렬한 리스트
    """
    answer = []    
    t_year, t_month, t_day = map(int, today.split("."))
    t_days = t_year*12*28 + t_month*28 + t_day

    # 약관 종류별 유효기간
    term_dict = defaultdict(int)
    for term in terms:
        term_type, term_period = term.split(" ")
        term_dict[term_type] = int(term_period)*28
    
    # 개인정보 수집날짜가 유효기간 이전인지 확인
    for idx, p in enumerate(privacies):
        p_date, p_type = p.split(" ")
        p_year, p_month, p_day = map(int, p_date.split("."))
        p_days = p_year*12*28 + p_month*28 + p_day
        if p_days + term_dict[p_type] <= t_days:
            answer.append(idx+1)

    return answer