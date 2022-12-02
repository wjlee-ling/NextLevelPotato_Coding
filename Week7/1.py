# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

N, M = map(int, input().split())
dict = {}
for i in range(N):
        dict[i+1] = 0

        for _ in range(M):
                for i in list(map(int, input().split()))[1:]:
                            dict[i] += 1

                            answer = (sorted(dict.items(), key=lambda x:(x[1],x[0]), reverse=True))
                            print(answer[0][0], end=' ')

                            for i in range(1, len(answer)):
                                    if answer[i][1] == answer[i-1][1]:
                                                print(answer[i][0], end=' ')
                                                    else:
                                                                break
