N = int(input())

if N == 1:
    print(1)
else:
    DP = [0] * (N+1)
    DP[0] = DP[1] = 1

    for i in range(2, N+1):
        DP[i] = (DP[i-2] + DP[i-1]) % 10
    print(DP[N])