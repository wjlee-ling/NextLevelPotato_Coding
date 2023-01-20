def solution(today, terms, privacies):
    answer = []
    
    def get_time(today):
        year, month, day = map(int, today.split('.'))
        return year * 12 * 28 + month * 28 + day
    
    print('today', get_time(today))
    
    dict = {}
    for term in terms:
        a, b = term.split(' ')
        dict[a] = int(b) * 28 
    #print(dict)
    
    
    for i, privacy in enumerate(privacies):
        date, types = privacy.split(' ')
        days = get_time(date)
        #print(days, dict[types], get_time(today))
        if days + dict[types] <= get_time(today):
            answer.append(i+1)

    
    return answer
