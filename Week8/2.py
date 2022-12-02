ing korean
N = int(input())
data = list(map(int, input().split()))

stack = []
for i in range(N):
        print(len(stack), end=' ')
            while stack and stack[-1] <= data[i]:
                            stack.pop()
                                stack.append(data[i])

                                #print(N, data)
