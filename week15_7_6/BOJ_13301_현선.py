n = int(input())
if n == 1:
    print(4)
elif n == 2:
    print(6)
elif n == 3:
    print(10)
else:
    dp = [0] * n
    dp[0] = 1
    dp[1] = 1
    for i in range(2,n):
        dp[i] = dp[i-1] + dp[i-2]
    result = (dp[n-1] * 3) + (dp[n-2] * 2) + (dp[n-3] * 2) + (dp[n-4] * 1)
    print(result)
