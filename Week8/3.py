
N = int(input())
data = list(map(int, input().split()))[0:N//2]
data.sort(reverse=True)
print(data)

answer = 0
if N % 2 == 0:
        for i in range(0, N//2, 2):
                    answer += data[i] * data[i+1]
                    print(answeru)
