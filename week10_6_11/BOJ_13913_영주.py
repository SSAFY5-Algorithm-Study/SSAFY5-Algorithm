# 13913. 숨바꼭질4 (골드4)

import sys
from collections import deque
input = sys.stdin.readline
DX = [-1, 1, 2]

def bfs(start):
    visited = [0] * 100001
    visited[start] = 1
    queue = deque([(start, [start])])
    while queue:
        x, movings = queue.popleft()
        for d in DX:
            nx = x+x if d == 2 else x+d
            if 0 <= nx <= 100000 and not visited[nx]:
                visited[nx] = visited[x] + 1
                if nx == k:
                    return visited[nx]-1, movings+[nx]
                queue.append((nx, movings+[nx]))

n, k = map(int, input().split())
if n >= k:
    print(n-k)
    print(*range(n, k-1, -1))
else:
    result, movings = bfs(n)
    print(result)
    print(*movings)
