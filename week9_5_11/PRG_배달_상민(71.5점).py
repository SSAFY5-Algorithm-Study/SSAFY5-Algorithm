'''
최소 거리를 구하는 문제이기 때문에 관련 알고리즘(다익스트라, kruskal, prim)중에 적절한 것을 선택
시작점이 1로 고정되어 있고, 시작점으로부터 K 시간내에 도착할 수 있는 곳들을 알아내면 된다.
시작점으로부터 모든 노드들에 대한 최저 비용을 구할 수 있는 '다익스트라' 알고리즘 사용

'''


def solution(N, road, K):
    
    D = [987654321 for _ in range(N + 1)]
    edges = [[] for _ in range(N + 1)]
    visited = [1] + [0 for _ in range(N)]
    # edge 표시
    for s, e, t in road:
        edges[s].append((e, t))
        edges[e].append((s, t))
    
    # # 1번 노드와 연결되어 있는 노드 거리 넣어주기
    for e, t in edges[1]:
        D[e] = t
    D[1], visited[1] = 0, 1
    
    
    
    # 노드 - 1만큼 반복
    for _ in range(N - 1):
        # 가장 작은 것(idx) 찾기
        min_value, min_idx = 987654321, 0
        for idx, value in enumerate(D):
            if value < min_value and not visited[idx]:
                min_value, min_idx = value, idx
                # print(min_value, min_idx)
        visited[min_idx] = 1
        
        for adj, adj_t in edges[min_idx]:
            D[adj] = min(D[adj], D[min_idx] + adj_t)
    
    answer = [d for d in D if d <= K]

    return len(answer)
