# 5567. 결혼식 (실버1)

import sys
from collections import deque
input = sys.stdin.readline


def bfs(start):
    count = 0
    visited = [0] * (n+1)
    visited[start] = 1
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if visited[node] > 2:
            continue
        for next_node in graph[node]:
            if visited[next_node] == 0:
                visited[next_node] = visited[node] + 1
                count += 1
                queue.append(next_node)
    return count


n, m = int(input()), int(input())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(bfs(1))
