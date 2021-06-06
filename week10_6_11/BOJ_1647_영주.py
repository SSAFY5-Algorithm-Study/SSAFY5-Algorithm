# 1647. 도시 분할 계획 (골드4)

import sys
input = sys.stdin.readline

def find_set(x):
    if x != parent[x]:
        parent[x] = find_set(parent[x])
    return parent[x]

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

parent = list(range(n+1))
total, count = [], 0
for c, a, b in edges:
    a_root, b_root = find_set(a), find_set(b)
    if a_root != b_root:
        parent[b_root] = a_root
        total.append(c)
        count += 1
        if count >= n-1:
            break
        
print(sum(total)-max(total))
