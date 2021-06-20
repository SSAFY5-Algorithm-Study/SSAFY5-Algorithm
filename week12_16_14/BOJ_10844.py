N = int(input())

cnt = 9 * (2**(N-1))
excluded = 0
for i in range(0, N):
    excluded = excluded * 2 + i

print(cnt, excluded)
print(cnt-excluded)