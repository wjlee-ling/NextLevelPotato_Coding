def solution(n):
    """
    1st try: (n-2) + (n-1) 
    """
    ls = [0,1,2] + [0] *(n-2)
    if n <= 2:
        return ls[n]
    m = 2
    while m < n:
        m+=1
        ls[m] = ls[m-1] + ls[m-2]
    
    return ls[n] % 1234567
