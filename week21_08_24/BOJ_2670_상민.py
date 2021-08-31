N = int(input())
numbers = list(float(input()) for _ in range(N))

DP = [[] for _ in range(N)]

for i in range(len(numbers)):
    if i == 0:
        DP[0] = numbers[i]
    # elif i == 1:
    #     DP[1] = max(DP[0] * numbers[i], numbers[i])
    else:
        DP[i] = max(DP[i-1] * numbers[i], numbers[i-1] * numbers[i], numbers[i])
print(round(max(DP), 4))