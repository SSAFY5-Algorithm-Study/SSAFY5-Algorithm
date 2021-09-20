N = int(input())
days = []
profits = []
DP = [0] * N
for _ in range(N):    
    day, profit = map(int, input().split())
    days.append(day)
    profits.append(profit)
for i in range(N):
    idx = i
    while True:
        if idx == i:
            DP[idx] = max(profits(idx), DP[idx])
        else:
            DP[idx] = max(profits(idx), DP[idx], DP)
        idx += days[idx]

