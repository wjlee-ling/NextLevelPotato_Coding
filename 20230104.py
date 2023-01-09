def solution(N, number):
    dp = [set() for _ in range(9)]
    
    for i in range(1, 9):
        dp[i].add(int(str(N)*i))
        for j in range(i//2+1):
            for d1 in dp[j]:
                for d2 in dp[i-j]:
                    dp[i].add(d1+d2)
                    dp[i].add(d1-d2)
                    dp[i].add(d1-d2)
                    dp[i].add(d1*d2)
                    if d1 != 0:
                        dp[i].add(d2//d1)
                    if d2 != 0:
                        dp[i].add(d1//d2)

        if number in dp[i]:
            return i
    print(dp)
    return -1
    

