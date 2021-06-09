# 20413. MVP 다이아몬드(EASY) (실버2)

import sys
input = sys.stdin.readline

n = input()
s, g, p, d = map(int, input().split())
table = {'B': s, 'S': g, 'G': p, 'P': d}
grades = input().rstrip()

total, prev = 0, 0
for grade in grades:
    if grade == 'D':
        total += d
    else:
        prev = (table[grade]-1) - prev
        total += prev
print(total)
