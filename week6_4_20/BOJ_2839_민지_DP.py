N = int(input())

if N == 3:
    cnt = 1
elif N == 4:
    cnt = -1
else:
    DP = [2000] * (N+1)
    DP[3] = 1
    DP[5] = 1
    for i in range(6, N+1):
        DP[i] = min(DP[i-3], DP[i-5]) + 1
    cnt = DP[N] if DP[N]<2000 else -1
print(cnt)