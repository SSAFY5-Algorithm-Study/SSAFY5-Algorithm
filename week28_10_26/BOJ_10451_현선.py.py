T = int(input())

def DFS(s):
    stack = [s]
    visited[s] = 1

    while stack:
        temp = stack.pop(-1)
        if visited[arr[temp]] == 0:
            stack.append(arr[temp])
            visited[arr[temp]] = 1

for _ in range(T):
    n = int(input())
    arr = [0] + list(map(int,input().split()))
    visited = [0] * (n+1)
    cnt = 0
    for i in range(1,n+1):
        if visited[i] == 0:
            DFS(i)
            # print(i)
            # print(visited)
            cnt += 1
    print(cnt)