# 14221. 편의점 (실버1)

import sys
from heapq import heappop, heappush
input = sys.stdin.readline
INF = int(1e9)


def dijkstra(start):
    distance = [INF] * (n+1)
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        dist, node = heappop(queue)
        if distance[node] < dist:
            continue
        for next_node, w in graph[node]:
            next_dist = dist + w
            if next_dist < distance[next_node]:
                distance[next_node] = next_dist
                heappush(queue, (next_dist, next_node))
    return distance


n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

p, q = map(int, input().split())
houses = sorted(map(int, input().split()))
stores = list(map(int, input().split()))

min_house, min_distance = houses[0], INF
for house in houses:
    distance = dijkstra(house)
    house_to_store = min(distance[store] for store in stores)
    if house_to_store < min_distance:
        min_house, min_distance = house, house_to_store

print(min_house)
