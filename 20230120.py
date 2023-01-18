'''
모든 달은 28일까지 (28일 다음 날은 1일)
유효기간인 날 전 날까지 보관가능(유효기간 날 파기)

today : 오늘 날짜 (YYYY.MM.DD)
terms : 약관의 유효기간 ("약관 종류(A~Z) 유효기간(달 수)")
privacies : 수집된 개인 정보("날짜(YYYY.MM.DD) 약관 종류")
ex. 2019.01.01 + 5달 = 2019.06.01이 아니라 2019.05.28까지 보관 가능

파기할 개인정보 번호를 오름차순 리스트로 return
'''
from collections import defaultdict

def solution(today, terms, privacies):
    answer = []
    
    year, month, date = map(int, today.split('.')) # 오늘 날짜
    
    term = defaultdict(int)
    for t in terms:
        types, lasting = t.split()
        term[types] = int(lasting)
    #print(term)
    
    for i in range(len(privacies)):
        dates, types = privacies[i].split()
        n_year, n_month, n_date = map(int, dates.split('.')) # 저장할 수 있는 마지막 날 다음 날
        n_month += term[types]
        while n_month > 12: # 유효기간(보관할 수 있는 달이 1 이상 100이하)
            n_month -= 12
            n_year += 1
        
        # 오늘 날짜와 저장할 수 있는 마지막 날 +1 비교
        if n_year > year: # 년도가 남았을 때
            continue
        if n_year == year:
            if n_month > month: # 년도는 안 남았는데 달이 남았을 때
                continue
            if n_month == month:
                if n_date > date: # 년도도, 달도 안남았는데 요일이 남았을 때 (포함해서는 안됨)
                    continue
        answer.append(i+1)
    return answer