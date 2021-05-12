# Summer/Winter Coding(~2018) 배달

from heapq import heappop, heappush
INF = int(1e9)


def dijkstra(start, N, graph):
    distance = [INF] * (N+1)
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        now_w, node = heappop(queue)
        if distance[node] < now_w:
            continue
        for next_node, next_w in graph[node]:
            new_distance = now_w + next_w
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                heappush(queue, (new_distance, next_node))
    return distance


def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    for s, e, w in road:
        graph[s].append((e, w))
        graph[e].append((s, w))

    return sum(t <= K for t in dijkstra(1, N, graph))
    

N = 5
road = [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]]
K = 3
print(solution(N, road, K))