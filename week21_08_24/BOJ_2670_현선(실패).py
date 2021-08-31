# 곱했는데, 더 작은값이 나온다? 안쓰는게 낫다
# 더 큰게 나온다? 뒤에걸 곱했을때 값이 더 커질 수 있는 가능성이 있음.
# dp[0] = 1.1
# 1.1 * 0.7 = 0.77 => dp[1] = 0.77
# 0.77 * 1.3 = 1.001 => dp[2] = 1.3
# 1.3 * 0.9 = 1.17 => dp[3] = 1.17
# 1.17 * 1.4 = 1.638 => dp[4] = 1.638
# 1.638 * 0.8 = 1.3104 => dp[5] = 1.3104
# .... 중에서 최대값 찾자.

n = int(input())
dp = [0] * n
# 첫 입력 dp배열에 집어넣기
dp[0] = float(input())
if n > 1:
    for i in range(1,n):
        num = float(input())
        if num > num * dp[i-1]:
            dp[i] = num
        else:
            dp[i] = num * dp[i-1]
        # if dp[i-1] < num * dp[i-1]:
        #     dp[i] = num * dp[i-1]
        # else:
        #     dp[i] = num
    # print(dp)
result = max(dp)
print(f'{ans:.3f}')
