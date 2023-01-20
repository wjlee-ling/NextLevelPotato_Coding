# https://school.programmers.co.kr/learn/courses/30/lessons/150370#qna

def solution(today, terms, privacies):
    def is_valid(privacy, due):
        due = int(due) # due within n months
        y,m,d = map(int, privacy.split("."))
        m = m + due
        d -= 1
        if d == 0: m -= 1; d=28
        if m > 12: m -= 12; y += 1
        return y,m,d
    def convert_to_date(y,m,d):
        # in days
        return d + m * 28 + y * 12 * 28
    
    answer = []
    term_dict = dict()
    for term in terms:
        k,v = term.split()
        term_dict[k] = int(v)
    ty, tm, td = map(int, today.split(".")) # today
    today = convert_to_date(ty,tm,td)
    for i, privacy in enumerate(privacies, start=1):
        p, contract = privacy.split()
        y,m,d = is_valid(p, term_dict[contract]) # valid until
        valid_until = convert_to_date(y,m,d)
        if valid_until < today:
            answer.append(i)
        
#         if y < ty:
#             answer.append(i)
#         elif y == ty and m < tm:
#             answer.append(i)
#         elif y == ty and m == tm and d < td:
#             answer.append(i)
    
    return answer
