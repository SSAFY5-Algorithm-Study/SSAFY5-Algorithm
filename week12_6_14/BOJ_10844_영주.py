# 10844. 쉬운 계단수 (실버1)

n = int(input())
memo = [[0]*(10) for _ in range(n+1)]
memo[1] = [0] + ([1]*9)

for i in range(2, n+1):
    for j in range(10):
        if not j:
            memo[i][j] = memo[i-1][j+1]
        elif j == 9:
            memo[i][j] = memo[i-1][j-1]
        else:
            memo[i][j] = memo[i-1][j-1] + memo[i-1][j+1]

print(sum(memo[-1]) % (10**9))