def solution(N, number):
    ns = {}
    for total in range(1, 9): # total # of Ns
        ns[total] = [int(str(N)*total)]

        for ind in range(1, 5): # (1,7), (2,6), (3,5), (4,4)
            if total - ind <=0:
                break
            for x in ns[ind]:
                for y in ns[total - ind]:
                    ns[total].append(x+y)
                    ns[total].append(x-y)
                    ns[total].append(y-x)
                    ns[total].append(x*y)
                    if x !=0: 
                        ns[total].append(y//x)
                    if y !=0:
                        ns[total].append(x//y)      
        ns[total] = list(set(ns[total]))
        if number in ns[total]:
            return total

    return -1
