# 1932. 정수삼각형 (실버1)

import sys
input = sys.stdin.readline

n = int(input())
numbers = [list(map(int, input().split())) for _ in range(n)]
for i in range(1, n):
    for j in range(i+1):
        if not j:
            numbers[i][j] += numbers[i-1][j]
        elif j == i:
            numbers[i][j] += numbers[i-1][j-1]
        else:
            numbers[i][j] += max(numbers[i-1][j-1], numbers[i-1][j])
print(max(numbers[-1]))