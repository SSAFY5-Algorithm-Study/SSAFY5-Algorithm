import sys
sys.stdin = open('input.txt', 'r')

N = int(input())

tri = [list(map(int, input().split())) for _ in range(N)]
max_sum = 0

k = 2
for r in range(1, N):
    for c in range(k):
        if c == 0:
            tri[r][c] = tri[r][c] + tri[r-1][c]
        elif r == c:
            tri[r][c] = tri[r][c] + tri[r-1][c-1]
        else:
            tri[r][c] = tri[r][c] + max(tri[r-1][c-1], tri[r-1][c])
    k += 1

print(max(tri[N-1]))
