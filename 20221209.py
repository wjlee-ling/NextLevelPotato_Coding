def solution(k, d):
    # try 1: (a^2k^2) + (b^2k^2) <= d^2
    # a^2+b^2 ~= d^2 / k^2 
    answer = 0
    limit = d**2 // k**2 # a^2 + b^2 , 4
    for a in range(int(limit**0.5)+1): 
        blimit = (limit - a**2)**0.5 
        answer += int(blimit) +1
        
    return answer
