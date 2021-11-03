N = int(input())

stairs = [int(input()) for _ in range(N)]
DP = [0 for _ in range(N)]

if N == 1:
    print(stairs[0])
elif N == 2:
    print(stairs[1])
elif N == 3:
    print(max(stairs[0]+stairs[2], stairs[1]+stairs[2]))
else:
    DP[0], DP[1], DP[2] = stairs[0], stairs[1], stairs[2] 

    for i in range(3, N):
        DP[i] = max((stairs[i] + stairs[i-1] + DP[i-3]),(stairs[i] + DP[i-2]))
    print(DP)
    print(DP[N-1])