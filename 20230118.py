## 귤 

def solution(k, tangerine):
    """
    sort해서 많이 있는 크기 위주로?
    """
    from collections import Counter
    answer = 0
    c = Counter(tangerine)

    for size, n in c.most_common():
        k -= n
        answer += 1
        if k <= 0:
            break
    return answer
