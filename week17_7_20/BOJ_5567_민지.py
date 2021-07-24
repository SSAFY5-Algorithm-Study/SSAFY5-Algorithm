N = int(input())
friends = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
visited[1] = 1

# 동기 관계 리스트 초기화
for _ in range(int(input())):
    a, b = map(int, input().split())
    friends[a].append(b)
    friends[b].append(a)

# 상근이의 친구들을 모두 세기
cnt = 0
for i in friends[1]:
    visited[i] = 1
    cnt += 1

# 상근이의 친구의 친구 중 상근이와 친구가 아닌 사람들 구하기 
for i in friends[1]:
    for j in friends[i]:
        if not visited[j]:
            visited[j] = 1
            cnt += 1

print(cnt)