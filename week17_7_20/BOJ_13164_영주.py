# 13164. 행복 유치원 (골드5)

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
heights = list(map(int, input().split()))
diffs = sorted(heights[i+1]-heights[i] for i in range(n-1))
for _ in range(k-1):
    diffs.pop()
print(sum(diffs))