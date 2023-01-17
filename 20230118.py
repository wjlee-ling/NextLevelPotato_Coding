from itertools import combinations

def solution(k, tangerine):
    answer = 0
    #tangerine = list(set(tangerine))
    tangerine.sort()

    
    result = [seq for i in range(k, 0, -1)
        for seq in combinations(tangerine, i)
            if sum(seq) == k]
            
    return len(result[0])
