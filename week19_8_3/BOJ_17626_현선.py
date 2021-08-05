#??????????????? 뭐지

n = int(input())
dp = [0] * (n+1)
dp[1] = 1
for i in range(1,n+1):
    dp[i] = dp[1] + dp[i-1]
    x = 2
    while (x*x <= i):
        dp[i] = min(dp[i], 1 + dp[i-(x*x)])
        x += 1
print(dp[n])