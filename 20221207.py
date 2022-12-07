def solution(n, times):
    # try 2: 심사시간 + 잔여시간 가장 낮은 데부터 채우기
    # 통과하나 몇몇 테케에서 시간초과
    # [0,0] (+[7,10]) => [7,0] (+[7,10]) => [7,10] (+[7,10]) => [14,10] (+[7,10]) => [14, 20]
    answer = 0
    rest = [0] * len(times)
    while n:
        # 심사+잔여 가장 낮은 데 > 차기 분기점
        temp = [t + r for t, r in zip(times, rest)]
        minidx = temp.index(min(temp))
        rest[minidx] += times[minidx]
        n -= 1
    answer = max(rest)

    # # try 1: [a,b] => [a,b, 2a,2b, 3a,3b ,....]
    # answer = 0
    # rest = {i: time for i, time in enumerate(times)}
    # flag = True
    # while n > 0:
    #     answer += 1
    #     # reduce a second from taken seats
    #     minidx = times.index(min(times))
    #     minidx_v = 1000000000
    #     for idx in range(len(times)):
    #         if times[idx] != rest[idx]:
    #             rest[idx] -= 1
    #             if rest[idx] == 0:
    #                 flag = True
    #                 if min(minidx_v, times[idx]) == times[idx]:
    #                     minidx = idx

    #     # if new seat is available
    #     if flag:
    #         rest[minidx] -= 1
    #         falg = False

    #     n -= 1
    return answer
