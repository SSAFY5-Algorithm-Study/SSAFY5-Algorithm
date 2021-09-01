# 1 -> 0번
# 2 -> 1번
# 3 -> 1번
# 4 -> 2로 나누어짐 -> 2일때의 횟수  : 2번
# 5 -> 1뺌 -> 4 -> 4일때의 횟수 : 3번
# 6 -> 3으로 나누어짐 -> 3일때의 횟수 : 2번
# 7 -> 1 뺌 -> 6 일때의 횟수 : 3
# 8 -> 2로 나누어짐 -> 4일때의 횟수 : 3번
# 9 -> 3로 나누어짐 -> 3일때의 횟수 : 2번
# 10 -> 2로 나누어짐 -> 5일때의 횟수 : 4번, 1 뺌 -> 9일때의 횟수 : 3번

n = int(input())

dp = [0] * 1000001
dp[1] = 0
dp[2] = 1
dp[3] = 1
for i in range(4,n+1):
    j = i - 1
    if not i % 3 and not i % 2:
        x = [dp[i//3] + 1, dp[i//2] + 1, dp[j]+1]
        dp[i] = min(x)
    elif not i % 3:
        dp[i] = min(dp[i//3] + 1, dp[j]+1)
    elif not i % 2:
        dp[i] = min(dp[i//2] + 1, dp[j]+1)
    else:
        dp[i] = dp[j] + 1

    # if not i % 3:
    #     dp[i] = dp[i//3] + 1
    # elif not i % 2:
    #     dp[i] = dp[i//2] + 1
    # else:
    #     j = i - 1
    #     if not j % 3:
    #         dp[i] = dp[j] + 1
    #     if not j % 2:
    #         dp[i] = dp[j] + 1

print(dp[n])


