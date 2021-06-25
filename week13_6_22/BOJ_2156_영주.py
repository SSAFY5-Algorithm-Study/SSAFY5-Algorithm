# 2156. 포도주 시식 (실버1)

import sys
input = sys.stdin.readline

n = int(input())
wine = [0] + [int(input()) for _ in range(n)]

if n == 1:
    print(wine[1])
else:
    dp = [0] * (n+1)
    dp[1] = wine[1]
    dp[2] = wine[1] + wine[2]
    for i in range(3, n+1):
        double_prev = dp[i-2] + wine[i]
        prev = dp[i-3] + wine[i-1] + wine[i]
        dp[i] = max(dp[i-1], double_prev, prev)
    print(dp[n])