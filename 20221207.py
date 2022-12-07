def solution(n, times):
    # try 1: [a,b] => [a,b, 2a,2b, 3a,3b ,....]
    answer = 0
    rest = {i: time for i, time in enumerate(times)}
    flag = True
    while n > 0:
        answer += 1
        # reduce a second from taken seats
        minidx = times.index(min(times))
        minidx_v = 1000000000
        for idx in range(len(times)):
            if times[idx] != rest[idx]:
                rest[idx] -= 1
                if rest[idx] == 0:
                    flag = True
                    if min(minidx_v, times[idx]) == times[idx]:
                        minidx = idx

        # if new seat is available
        if flag:
            rest[minidx] -= 1
            falg = False

        n -= 1
    return answer
