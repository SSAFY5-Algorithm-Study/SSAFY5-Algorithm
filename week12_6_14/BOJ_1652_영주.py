# 1652. 누울 자리를 찾아라 (브론즈1)

import sys
input = sys.stdin.readline

def count_lying_space(room):
    space = 0
    for line in room:
        for empty in line.split('X'):
            if len(empty) >= 2:
                space += 1
    return space

n = int(input())
room = [input().rstrip() for _ in range(n)]
rotated_room = [''.join(line) for line in zip(*room)]
print(count_lying_space(room), count_lying_space(rotated_room))