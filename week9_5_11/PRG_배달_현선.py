def solution(N, road, K):
    answer = 0
    # 접근 : 다익스트라로 풀면되겠네
    # 거리가 K 이하인 곳만 카운트 하면 끝날듯
    # BFS도 가능할듯
    AL = [[] for _ in range(N+1)]
    for i in range(len(road)):
        # 임의의 두 마을간에 항상 이동이 가능하다고 했으므로 양방향 처리
        AL[road[i][0]].append([road[i][1], road[i][2]])
        AL[road[i][1]].append([road[i][0], road[i][2]])
    distance = [10001 * 51] * (N+1)
    visited = [0] * (N+1)
    distance[1] = 0
    visited[1] = 1
    for jeongjeom in AL[1]:
        distance[jeongjeom[0]] = jeongjeom[1]
    
    i = 0
    while i < N-1:
        min_dist = 10001 * 51
        min_idx = 0
        for j in range(N+1):
            if visited[j] == 1:
                continue
            if distance[j] < min_dist:
                min_dist = distance[j]
                min_idx = j
        
        visited[min_idx] = 1
        for jeongjeom in AL[min_idx]:
            distance[jeongjeom[0]] = min(distance[jeongjeom[0]], distance[min_idx] + jeongjeom[1])
        
        i += 1
        
    for dist in distance:
        if dist <= K:
            answer += 1
    return answer