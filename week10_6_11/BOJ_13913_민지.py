import sys
input = sys.stdin.readline

[-1, 0, 3, -1, 1]
def find_path(pa, x):
    moves = 0
    path = [x]
    while pa[x] != -1:
        path.insert(0, pa[x])
        x = pa[x]
        moves += 1
    return moves, path

def bfs(N, K):
    pa = [-1] * 100001
    moves = [lambda x:x+1, lambda x:x-1, lambda x:2*x]
    queue = [N]

    while queue:
        current = queue.pop(0)
        for i in range(3):
            nxt = moves[i](current)

            if 0 <= nxt <= 100000 and pa[nxt] == -1 and nxt != N:
                pa[nxt] = current
                queue.append(nxt)
                if nxt == K:
                    pa[nxt] = current
                    moves, path = find_path(pa, K)
                    return moves, path

N, K = map(int, input().split())

moves, path = bfs(N, K)
print(moves)
print(" ".join(map(str, path)))