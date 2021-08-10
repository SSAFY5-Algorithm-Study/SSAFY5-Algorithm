# 1654. 랜선 자르기 (실버3)

import sys
input = sys.stdin.readline

k, n = map(int, input().split())
cables = [int(input()) for _ in range(k)]

start, end = 1, max(cables)
while start <= end:
    mid = (start+end) // 2
    total = sum(cable//mid for cable in cables)
    if total < n:
        end = mid - 1
    else:
        start = mid + 1
print(end)