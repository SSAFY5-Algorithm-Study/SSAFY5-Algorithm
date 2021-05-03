# 동전 0
# Ai는 Ai-1의 배수라는 조건이 있어서 DP를 쓰지 않아도 풀이 가능
import sys
sys.stdin = open('input.txt', 'r')

N, K = map(int, input().split())

coins = []
for _ in range(N):
    coins.append(int(input()))

cnt = 0
while K > 0:
    for i in range(len(coins)-1, -1, -1):
        if K >= coins[i]:
            cnt += 1
            K -= coins[i]
            break

print(cnt)