N = int(input())
DP = [[0, 0] for _ in range(46)]
DP[1] = [0, 1]

for i in range(2, N + 1):
    DP[i][0] = DP[i-1][1]
    DP[i][1] = DP[i-1][0] + DP[i-1][1]

print(' '.join(map(str, DP[N])))