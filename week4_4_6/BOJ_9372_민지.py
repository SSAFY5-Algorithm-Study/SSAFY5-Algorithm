T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    schedules = [[] for _ in range(N+1)]

    for _ in range(M):
        s, e = map(int, input().split())
        schedules[s].append(e)
        schedules[e].append(s)
    
    visited = [1, 1] + [0] * (N-1)
    stack = [1]
    cnt = -1
    while stack:
        idx = stack.pop()
        cnt += 1
        for i in schedules[idx]:
            if not visited[i]:
                stack.append(i)
                visited[i] = 1
    print(cnt)