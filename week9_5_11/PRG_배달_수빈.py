def solution(N, road, K):
    # AL = [[] for _ in range(N + 1)]
    city = {i: {} for i in range(N+1)}

    for s, e, w in road:
        # 두 마을을 연결하는 도로 여러 개 중 시간이 적은 걸 저장해야 한다.
        if s in city and e in city[s]:
            if city[s][e] > w:
                city[s][e] = w
                city[e][s] = w
        else:
            city[s][e] = w
            city[e][s] = w

    # 다익스트라
    check = [0] * (N + 1)
    D = [987654321] * (N + 1)
    check[1] = 1
    D[1] = 0
    
    for v in city[1]:
        D[v] = city[1][v]
    
    for _ in range(N):
        min_w = 987654321
        min_idx = 0
        for i in range(N + 1):
            if not check[i] and D[i] < min_w:
                min_w = D[i]
                min_idx = i
        
        check[min_idx] = 1
    
        for v in city[min_idx]:
            D[v] = min(D[v], D[min_idx] + city[min_idx][v])
    
    answer = 0

    for d in D:
        if d <= K:
            answer += 1
    
    return answer