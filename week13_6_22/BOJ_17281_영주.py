# 17281. ⚾ (골드4)

import sys
from itertools import permutations
input = sys.stdin.readline
HITS = 1
DOUBLE = 2
TRIPLE = 3
HOMERUN = 4
OUT = 0


players = [list(map(int, input().split())) for _ in range(int(input()))]
hitters = [1, 2, 3, 5, 6, 7, 8, 9]
max_score = 0

for order in permutations(hitters, 8):
    score = 0
    now_player = 0
    hit_order = sorted([(i, hit) for i, hit in enumerate((4,) + order)], key=lambda x: x[1])
    print(hit_order)
    for player in players:
        out = 0
        b1, b2, b3 = 0, 0, 0
        while out < 3:
            now_score = player[hit_order[now_player][0]]
            if now_score == OUT:
                out += 1
            elif now_score == HITS:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif now_score == DOUBLE:
                score += b2 + b3
                b1, b2, b3 = 0, 1, b1
            elif now_score == TRIPLE:
                score += b1 + b2 + b3
                b1, b2, b3 = 0, 0, 1
            elif now_score == HOMERUN:
                score += b1 + b2 + b3 + 1
                b1, b2, b3 = 0, 0, 0
            now_player += 1
            if now_player > 8:
                now_player = 0
    max_score = max(max_score, score)

print(max_score)

