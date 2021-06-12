# 11581. 구호물자 (실버1)

import sys
input = sys.stdin.readline

def is_cycle(node):
    for next_node in graph[node]:
        if visited[next_node]:
            return True
        visited[next_node] = True
        if is_cycle(next_node):
            return True
        visited[next_node] = False
    return False

n = int(input())
graph = [[] for _ in range(n+1)]
for i in range(1, n):
    _ = input()
    graph[i].extend(map(int, input().split()))

visited = [False] * (n+1)
print('CYCLE') if is_cycle(1) else print('NO CYCLE')
