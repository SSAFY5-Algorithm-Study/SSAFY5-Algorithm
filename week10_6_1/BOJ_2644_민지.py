import sys
sys.stdin = open('input.txt', 'r')


def calculate_chonsu(s, e):
    visited = [0] * (N+1)
    visited[s] = 1

    queue = [[s, 0]]
    while queue:
        current, level = queue.pop(0)
        if current == e:
            return level

        for i in AL[current]:
            if not visited[i]:
                queue.append([i, level+1])
                visited[i] = 1
    return -1


# 사람 수
N = int(input())
# 촌수를 계산해야 되는 두 사람
A, B = map(int, input().split())
# 관계 수
M = int(input())

AL = [[] for _ in range(N+1)]
for _ in range(M):
    x, y = map(int, input().split())
    AL[x].append(y)
    AL[y].append(x)

result = calculate_chonsu(A, B)
print(result)