n = int(input())
dp = [0] * (n+1)

# 점수 리스트
step = [0] * (n+1)

# 입력받은 점수 리스트에 넣기
for i in range(n):
    step[i] = int(input())

# dp[0] = 첫번째 점수
dp[0] = step[0]
# dp[1] = 첫번째 점수 + 두번째 점수
dp[1] = step[0] + step[1]

# dp[2] = 첫번째 계단 + 2 계단 올랐을때, 두번째 계단 밟고 한계단 올랐을 때 더 큰값 
if step[0] + step[2] > step[1] + step[2]:
    dp[2] = step[0] + step[2]
else:
    dp[2] = step[0] + step[1]

for i in range(3,n):
    # 마지막 계단 직전을 밟지 않는 경우
    if dp[i-2] + step[i] > dp[i-3] + step[i-1] + step[i]:
        dp[i] = dp[i-2] + step[i]
    # 마지막 계단 직전 계단 밟은 경우
    else:
        dp[i] = dp[i-3] + step[i-1] + step[i]

print(dp[n-1])