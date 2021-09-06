# (DP[n-1] + 1, DP[n/2] + 1, DP[n/3] + 1)

def isDividedByTwo(value):
    if value % 2:
        return 0
    return value // 2

def isDividedByThree(value):
    if value % 3:
        return 0
    return value // 3

N = int(input())
DP = [987654321] + [0] * N
for i in range(2, N + 1):
    DP[i] = min(DP[i-1] + 1, DP[isDividedByTwo(i)] + 1, DP[isDividedByThree(i)] + 1)
print(DP[-1])