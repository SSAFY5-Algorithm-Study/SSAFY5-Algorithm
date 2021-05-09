def solution(n, s, a, b, fares):
    answer = 0
    # n : 지점 개수
    # s : 출발지점
    # a : A의 도착지점
    # b : B의 도착지점
    # fares = 지점사이의 예상 택시요금
    # 다익스트라로 접근해보자
    AL = [[] for _ in range(n+1)]
    for gansun in fares:
        # 양방향
        AL[gansun[0]].append([gansun[1],gansun[2]])
        AL[gansun[1]].append([gansun[0],gansun[2]])
    visited = [0] * (n+1)
    distance = [10001*n] * (n+1)
    visited[s] = 1
    distance[s] = 0
    # 시작점에 연결된 애들의 거리 갱신
    for gansun in AL[s]:
        distance[gansun[0]] = gansun[1]
    
    # distance 배열에서 제일 작은값 가져오고, 방문처리.
    i = 0
    while i < n-1:
        min_v = 10001*n
        min_idx = 0
        for j in range(n+1):
            if visited[j] < min_v:
                min_v = distance[j]
                min_idx = j
        visited[min_idx] = 1
        
        # 가져온 정점과 연결된 정점들을 탐색하면서,
        # 현재 distance 배열에 저장된 값과 
        # "가져온 정정 거리정보 + 둘 사이의거리" 
        # 중 더 작은 값을 dinstance 배열에 갱신
        for node in AL[min_idx]:
            distance[node[0]] = min(distance[node[0]], distance[min_idx] + node[1])
        i += 1
    print(distance[a])
    print(distance[b])
    
    return answer